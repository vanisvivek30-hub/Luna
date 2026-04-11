/**
 * IndustrySolve API Service
 * Centralized API communication layer between frontend and backend
 */

// Load configuration (will be updated by run_with_ngrok.py)
let API_BASE_URL = 'https://luna-2-62hl.onrender.com/api'; // Default fallback

// Try to load config from config.js if it exists
try {
  // For browser environment, check if API_CONFIG is available
  if (typeof window !== 'undefined' && typeof API_CONFIG !== 'undefined') {
    API_BASE_URL = API_CONFIG.baseUrl;
    console.log('✅ Loaded API config from config.js');
  } else {
    // Fallback: try to determine from current URL
    const currentHost = window.location.host;
    const currentProtocol = window.location.protocol;

    if (currentHost.includes('localhost') || currentHost.includes('127.0.0.1')) {
      API_BASE_URL = 'https://luna-2-62hl.onrender.com/api';
    } else {
      // Assume ngrok or production - API should be on same domain
      API_BASE_URL = `${currentProtocol}//${currentHost}/api`;
    }
    console.log('⚠️  Using fallback API detection');
  }
} catch (error) {
  console.warn('Could not load API config, using defaults:', error);
}

console.log('🌐 API Base URL:', API_BASE_URL); // Debug log

// ════════════ AUTHENTICATION ENDPOINTS ════════════

/**
 * Sign up a new user
 * @param {Object} userData - User registration data
 * @param {string} userData.email - User email
 * @param {string} userData.password - User password (min 8 chars)
 * @param {string} userData.name - User full name
 * @param {string} userData.role - 'student' or 'org'
 * @param {string} userData.college - College name (for students)
 * @param {string} userData.domain - Domain of expertise (for students)
 * @param {string} userData.org_name - Organization name (for orgs)
 * @param {string} userData.industry - Industry type (for orgs)
 * @returns {Promise<Object>} API response with success flag and user data
 */
async function apiSignup(userData) {
  try {
    const response = await fetch(`${API_BASE_URL}/signup`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || `HTTP ${response.status}: Signup failed`);
    }

    // Store user in session
    if (data.success && data.user) {
      sessionStorage.setItem('signedUser', JSON.stringify({
        role: data.user.role,
        email: data.user.email,
        name: data.user.name,
        id: data.user.id
      }));
    }

    return data;
  } catch (error) {
    console.error('Signup error:', error);
    return {
      success: false,
      message: error.message || 'Connection error. Make sure backend is running on Render.'
    };
  }
}

/**
 * Sign in an existing user
 * @param {Object} credentials - Login credentials
 * @param {string} credentials.email - User email
 * @param {string} credentials.password - User password
 * @param {string} credentials.role - 'student' or 'org' (optional, for role validation)
 * @returns {Promise<Object>} API response with success flag and user data
 */
async function apiSignin(credentials) {
  try {
    const response = await fetch(`${API_BASE_URL}/signin`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(credentials)
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || `HTTP ${response.status}: Sign in failed`);
    }

    // Store user in session
    if (data.success && data.user) {
      sessionStorage.setItem('signedUser', JSON.stringify({
        role: data.user.role,
        email: data.user.email,
        name: data.user.name,
        id: data.user.id
      }));
    }

    return data;
  } catch (error) {
    console.error('Sign in error:', error);
    return {
      success: false,
      message: error.message || 'Connection error. Make sure backend is running on Render.'
    };
  }
}

// ════════════ USER ENDPOINTS ════════════

/**
 * Fetch user profile by email
 * @param {string} email - User email address
 * @returns {Promise<Object>} API response with user data
 */
async function apiGetUser(email) {
  try {
    const response = await fetch(`${API_BASE_URL}/user/${encodeURIComponent(email)}`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' }
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || `HTTP ${response.status}: Failed to fetch user`);
    }

    return data;
  } catch (error) {
    console.error('Get user error:', error);
    return {
      success: false,
      message: error.message || 'Failed to fetch user profile'
    };
  }
}

/**
 * Fetch all users (admin/organization endpoint)
 * @returns {Promise<Object>} API response with array of users
 */
async function apiGetAllUsers() {
  try {
    const response = await fetch(`${API_BASE_URL}/users`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' }
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.message || `HTTP ${response.status}: Failed to fetch users`);
    }

    return data;
  } catch (error) {
    console.error('Get all users error:', error);
    return {
      success: false,
      message: error.message || 'Failed to fetch users'
    };
  }
}

// ════════════ HEALTH CHECK ════════════

/**
 * Check backend API health status
 * @returns {Promise<Object>} API response with status
 */
async function apiHealthCheck() {
  try {
    const response = await fetch(`${API_BASE_URL}/health`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json' }
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    return data;
  } catch (error) {
    console.error('Health check error:', error);
    return {
      status: 'Backend unavailable',
      error: error.message
    };
  }
}

// ════════════ SESSION MANAGEMENT ════════════

/**
 * Get currently signed-in user from session storage
 * @returns {Object|null} User object or null if not signed in
 */
function getCurrentUser() {
  try {
    const saved = sessionStorage.getItem('signedUser');
    return saved ? JSON.parse(saved) : null;
  } catch (err) {
    console.error('Error parsing session user:', err);
    return null;
  }
}

/**
 * Clear current user session
 */
function logoutUser() {
  sessionStorage.removeItem('signedUser');
}

/**
 * Check if user is currently signed in
 * @returns {boolean} True if user is signed in
 */
function isUserSignedIn() {
  return getCurrentUser() !== null;
}

/**
 * Check if current user is an organization
 * @returns {boolean} True if user is an organization
 */
function isCurrentUserOrg() {
  const user = getCurrentUser();
  return user?.role === 'org';
}

/**
 * Check if current user is a student
 * @returns {boolean} True if user is a student
 */
function isCurrentUserStudent() {
  const user = getCurrentUser();
  return user?.role === 'student';
}

// ════════════ UTILITY FUNCTIONS ════════════

/**
 * Validate email format
 * @param {string} email - Email to validate
 * @returns {boolean} True if email is valid
 */
function isValidEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

/**
 * Validate password strength
 * @param {string} password - Password to validate
 * @returns {Object} Validation result with score and feedback
 */
function validatePassword(password) {
  let score = 0;
  const feedback = [];

  if (password.length >= 8) {
    score++;
  } else {
    feedback.push('At least 8 characters required');
  }

  if (/[A-Z]/.test(password)) {
    score++;
  } else {
    feedback.push('Add uppercase letters');
  }

  if (/[0-9]/.test(password)) {
    score++;
  } else {
    feedback.push('Add numbers');
  }

  if (/[^A-Za-z0-9]/.test(password)) {
    score++;
  } else {
    feedback.push('Add special characters');
  }

  const strength = ['Weak', 'Fair', 'Good', 'Strong', 'Very Strong'][score] || 'Weak';

  return {
    score,
    strength,
    feedback,
    isValid: score >= 2
  };
}

/**
 * Format user name from email
 * @param {string} email - Email address
 * @returns {string} Formatted name
 */
function getNameFromEmail(email) {
  const raw = email.split('@')[0].replace(/[._\-]/g, ' ');
  return raw
    .split(' ')
    .filter(Boolean)
    .map(part => part.charAt(0).toUpperCase() + part.slice(1))
    .join(' ') || 'User';
}

// ════════════ ERROR HANDLING ════════════

/**
 * Display an error message to user
 * @param {string} message - Error message
 * @param {number} duration - Duration in ms (default 3000)
 */
function showErrorMessage(message, duration = 3000) {
  const alert = document.createElement('div');
  alert.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    background: #ef4444;
    color: white;
    padding: 12px 20px;
    border-radius: 6px;
    z-index: 9999;
    font-size: 14px;
    max-width: 300px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  `;
  alert.textContent = message;
  document.body.appendChild(alert);

  setTimeout(() => alert.remove(), duration);
}

/**
 * Display a success message to user
 * @param {string} message - Success message
 * @param {number} duration - Duration in ms (default 3000)
 */
function showSuccessMessage(message, duration = 3000) {
  const alert = document.createElement('div');
  alert.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    background: #10b981;
    color: white;
    padding: 12px 20px;
    border-radius: 6px;
    z-index: 9999;
    font-size: 14px;
    max-width: 300px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  `;
  alert.textContent = message;
  document.body.appendChild(alert);

  setTimeout(() => alert.remove(), duration);
}

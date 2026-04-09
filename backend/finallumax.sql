CREATE DATABASE IF NOT EXISTS lumaxdb;
USE lumaxdb;

-- Added AUTO_INCREMENT and PRIMARY KEYs
CREATE TABLE user_info(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50),
    user_email VARCHAR(100) UNIQUE, -- Unique prevents duplicate accounts
    user_pass VARCHAR(255),        -- Increased for secure password hashing
    user_role VARCHAR(20)          -- 'student', 'ngo', or 'company'
);

CREATE TABLE problems(
    problem_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    user_description TEXT,         -- TEXT allows for longer project briefs
    posted_by_id INT,              -- Link to the NGO's user_id
    FOREIGN KEY (posted_by_id) REFERENCES user_info(user_id)
);

CREATE TABLE Applications(
    app_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    problem_id INT,
    status VARCHAR(20) DEFAULT 'pending',
    FOREIGN KEY (student_id) REFERENCES user_info(user_id),
    FOREIGN KEY (problem_id) REFERENCES problems(problem_id)
);

CREATE TABLE Submissions(
    sub_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    problem_id INT,
    git_link VARCHAR(255),
    status_ VARCHAR(30),
    FOREIGN KEY (student_id) REFERENCES user_info(user_id),
    FOREIGN KEY (problem_id) REFERENCES problems(problem_id)
);
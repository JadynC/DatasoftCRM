CREATE TABLE Campaigns (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
start_date DATE,
end_date DATE,
budget DECIMAL(10,2),
status ENUM('planned', 'active', 'completed')
);

CREATE TABLE Leads (
id INT PRIMARY KEY AUTO_INCREMENT,
full_name VARCHAR(255),
email VARCHAR(255),
phone VARCHAR(20),
campaign_id INT,
FOREIGN KEY (campaign_id) REFERENCES Campaigns(id)
);

CREATE TABLE Emails (
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(255),
subject VARCHAR(255),
body TEXT,
campaign_id INT,
FOREIGN KEY (campaign_id) REFERENCES Campaigns(id)
);

CREATE TABLE Tickets (
id INT PRIMARY KEY AUTO_INCREMENT,
title VARCHAR(255),
description TEXT,
created_at DATETIME,
status ENUM('open', 'closed') DEFAULT 'open'
);

CREATE TABLE TicketComments (
id INT PRIMARY KEY AUTO_INCREMENT,
ticket_id INT,
comment TEXT,
created_at DATETIME,
FOREIGN KEY (ticket_id) REFERENCES Tickets(id)
);

CREATE TABLE KnowledgeBase (
id INT PRIMARY KEY AUTO_INCREMENT,
title VARCHAR(255),
content TEXT
);

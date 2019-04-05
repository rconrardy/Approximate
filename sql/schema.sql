/* tasks table */
CREATE TABLE tasks(
  /* id, integer */
  id INTEGER AUTOINCREMENT,
  /* name, at most 20 chars */
  name VARCHAR(20) NOT NULL,
  /* description, at most 1024 chars */
  description VARCHAR(1024) NOT NULL,
  /* created, timestamp */
  created Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  /* task_id, primary key */
  PRIMARY KEY(task_id)
);

/* categories table */
CREATE TABLE categories(
  /* category_id, integer */
  id INTEGER AUTOINCREMENT,
  /* category_name, at most 20 chars */
  name VARCHAR(20) NOT NULL,
  /* description */
  description VARCHAR(1024) NOT NULL,
  /* created, timestamp */
  created Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  /* category_id, primary key */
  PRIMARY KEY(category_id)
);

/* tasks_categories */
CREATE TABLE tasks_categories(
  /* task_id, integer */
  task_id INTEGER NOT NULL,
  /* category_id, integer */
  category_id INTEGER NOT NULL,
  /* created, timestamp */
  created Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  /* tuple (task_id, category_id), primary key */
  PRIMARY KEY(task_id, category_id),
  /* task_id, foreign key to categories */
  FOREIGN KEY(task_id)
    REFERENCES categories(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  /* category_id, foreign key to tasks */
  FOREIGN KEY(category_id)
    REFERENCES tasks(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)

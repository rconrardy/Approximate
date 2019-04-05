INSERT INTO tasks(id, name, description)
VALUES (1, 'Umich ENGR Memo', 'Memo for the University of Michigan.');

INSERT INTO tasks(id, name, description)
VALUES (2, 'Umich CS Memo', 'Memo for the University of Michigan.');

INSERT INTO tasks(id, name, description)
VALUES (3, 'Tax Return Form', 'Fill out the tax return forms.');

INSERT INTO categories(id, name, description)
VALUES (1, 'Memo', 'Tag all Memo tasks with this.');

INSERT INTO categories(id, name, description)
VALUES (2, 'Umich', 'Tag all Umich tasks with this.');

INSERT INTO categories(id, name, description)
VALUES (3, 'ENGR', 'Tag all engineering tasks with this.');

INSERT INTO categories(id, name, description)
VALUES (4, 'CS', 'Tag all computer science tasks with this.');

INSERT INTO categories(id, name, description)
VALUES (5, 'Tax', 'Tag all tax tasks with this.');

INSERT INTO categories(id, name, description)
VALUES (6, 'Form', 'Tag all form tasks with this.');

INSERT INTO tasks_categories(task_id, category_id)
VALUES (1, 1);

INSERT INTO tasks_categories(task_id, category_id)
VALUES (1, 2);

INSERT INTO tasks_categories(task_id, category_id)
VALUES (1, 3);

INSERT INTO tasks_categories(task_id, category_id)
VALUES (2, 1);

INSERT INTO tasks_categories(task_id, category_id)
VALUES (2, 2);

INSERT INTO tasks_categories(task_id, category_id)
VALUES (2, 4);

INSERT INTO tasks_categories(task_id, category_id)
VALUES (3, 5);

INSERT INTO tasks_categories(task_id, category_id)
VALUES (3, 6);

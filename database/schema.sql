CREATE SCHEMA IF NOT EXISTS `the_reading_cauldron_db`
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE `the_reading_cauldron_db`;

CREATE TABLE IF NOT EXISTS `users` (
    `user_id` INT AUTO_INCREMENT PRIMARY KEY,
    `user_name` VARCHAR(50) NOT NULL UNIQUE,
    `user_email` VARCHAR(100) NOT NULL UNIQUE,
    `user_password_hash` VARCHAR(255) NOT NULL,
    `user_created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `books` (
    `book_id` INT AUTO_INCREMENT PRIMARY KEY,
    `book_title` VARCHAR(150) NOT NULL,
    `book_author` VARCHAR(120) NOT NULL,
    `book_isbn` VARCHAR(30) UNIQUE,
    `book_description` TEXT,
    `book_pages` INT,
    `book_language` VARCHAR(50),
    `book_category` VARCHAR(80),
    `book_cover_url` VARCHAR(255),
    `book_created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `library` (
    `library_id` INT AUTO_INCREMENT PRIMARY KEY,
    `library_user_id` INT NOT NULL,
    `library_book_id` INT NOT NULL,

    `library_status` ENUM(
        'quiero_leer',
        'pendiente',
        'leyendo',
        'terminado',
        'abandonado'
    ) DEFAULT 'pendiente',

    `library_format` ENUM(
        'papel',
        'digital',
        'audiolibro'
    ) DEFAULT 'papel',

    `library_rating` TINYINT UNSIGNED,
    `library_current_page` INT DEFAULT 0,
    `library_start_date` DATE,
    `library_finish_date` DATE,
    `library_notes` TEXT,
    `library_favorite` BOOLEAN DEFAULT FALSE,

    `library_ownership` ENUM(
        'propio',
        'prestado',
        'biblioteca',
        'no_lo_tengo'
    ) DEFAULT 'propio',

    `library_created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `library_updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT `fk_library_users`
        FOREIGN KEY (`library_user_id`)
        REFERENCES `users`(`user_id`)
        ON DELETE CASCADE,

    CONSTRAINT `fk_library_books`
        FOREIGN KEY (`library_book_id`)
        REFERENCES `books`(`book_id`)
        ON DELETE CASCADE,

    CONSTRAINT `unique_library_book`
        UNIQUE (
            `library_user_id`,
            `library_book_id`,
            `library_format`
        ),

);

ALTER TABLE `library`
ADD CONSTRAINT `chk_library_rating`
CHECK (
    `library_rating` IS NULL 
    OR `library_rating` BETWEEN 0 AND 5
);
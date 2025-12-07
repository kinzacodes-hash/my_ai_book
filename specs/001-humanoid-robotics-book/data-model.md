# Data Model: Humanoid Robotics Book

## Entities

### User
- **id**: `UUID` (Primary Key)
- **name**: `string`
- **email**: `string` (unique)
- **password_hash**: `string`
- **progress**: `JSONB` (map of module IDs to completion status)
- **background_profile**: `string` (e.g., "AI engineer", "student")

### Book
- **id**: `UUID` (Primary Key)
- **title**: `string`
- **modules**: `JSONB` (array of module objects, each with `id`, `title`, `chapters`)

### Chapter
- **id**: `UUID` (Primary Key)
- **title**: `string`
- **content**: `text`
- **module_id**: `UUID` (Foreign Key to Module)

### Module
- **id**: `UUID` (Primary Key)
- **title**: `string`
- **book_id**: `UUID` (Foreign Key to Book)

## Relationships
- A **Book** has many **Modules**.
- A **Module** has many **Chapters**.
- A **User** has a **progress** JSONB field that tracks their completion status for each **Module**.

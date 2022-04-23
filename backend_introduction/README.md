# Introduction to Backend Development

[platzi](https://platzi.com/cursos/introduccion-backend/) | Facundo García Martoni

<br>

Learn the basics to understand how the web works from the inside. Then you can start your way into backend development with the programming language of your choice.

- Learn the difference between framework and library
- Learn the concept of server and its characteristics
- Analyze the HTTP protocol
- Understand the meaning of frontend and backend

## Foundations of web development

- Frontend and backend: concepts and most commonly used frameworks
- Framework vs. Library
- Connecting fronted and backend: API & JSON
- HTTP Requests and Responses
- Web Application Development flow
- Server: Cloud Computing Hosting

## API desing

- Twitter: API design and sketch

| **Protocol** | **Domain**  | **Endpoints** |
| :----------: | :---------: | :-----------: |
|   http://    | twitter.com |  /api/tweets  |
|              |             |  /api/users   |

- Endpoints for the Tweets module

  - GET `/tweets` - Displays all tweets (read)
  - POST `/tweets` - Publish a new tweet (create)
  - GET `/tweets/{tweetid}` - Displays a tweet by id (read)
  - PUT `/tweets/{tweet-id}` - Edit a tweet (update)
  - DELETE `/tweets/{tweet-id}` - Deletes a tweet (delete)

- Endpoints for the Users module

  - GET `/users` - Displays all users (read)
  - POST `/users` - Register a new user (create)
  - GET `/users/{user-id}` - Displays an user by id (read)
  - PUT `/users/{user-id}` - Edit an user profile (update)
  - DELETE `/users/{user-id}` - Deletes an user (delete)

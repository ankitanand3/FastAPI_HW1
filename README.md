# FastAPI Mastery: Guided Practice & Projects

A comprehensive practice guide designed to build deep understanding through progressive challenges. Each homework and project includes a Claude Code prompt for guided learning (like a TA would provide).

---

## 📚 HOMEWORK ASSIGNMENTS

### **Homework 1: API Fundamentals & FastAPI Basics**
**Duration:** 3-4 hours  
**Focus:** Understanding APIs, HTTP methods, and building your first FastAPI applications

#### Learning Objectives:
- Master API concepts and REST principles
- Understand request/response cycles
- Build basic FastAPI endpoints with proper routing
- Implement path and query parameters

#### Challenge Tasks:

**Task 1.1: Book Library API**
Build a book management API with the following requirements:
- Create endpoints for GET, POST, PUT, DELETE operations
- Implement path parameters for book ID
- Add query parameters for filtering (genre, author, year)
- Return proper HTTP status codes
- Use Pydantic models for request/response validation

**Task 1.2: Student Grade Calculator API**
- Create an API that accepts student information (name, scores in 5 subjects)
- Calculate GPA, letter grade, and rank
- Implement validation (scores between 0-100)
- Return detailed response with calculations
- Add an endpoint to retrieve all students sorted by GPA

#### Success Criteria:
- [ ] All endpoints return correct status codes
- [ ] Pydantic models validate inputs properly
- [ ] Query parameters work for filtering
- [ ] API documentation auto-generates at /docs
- [ ] No hardcoded values, use proper data structures

#### Claude Code Prompt for Homework 1:
```
I'm working on Homework 1 for FastAPI fundamentals. I need to build a Book Library API and Student Grade Calculator API.

Current state: [Describe what you've built so far]
Stuck on: [Specific challenge you're facing]

Please guide me like a university TA would:
1. Ask me questions about my approach before giving hints
2. Point me to relevant FastAPI documentation sections
3. Help me think through the design decisions (what HTTP method to use and why)
4. If I'm implementing Pydantic models, ask me what validations I think are necessary
5. For errors, help me debug by asking what the error message means and what might cause it
6. Suggest edge cases I should test but don't write the test code
7. When I'm close to the solution, give me conceptual nudges rather than direct answers

Don't write complete code for me - instead, help me understand the concepts so I can implement it myself.
```

---

### **Homework 2: Advanced Routing & Data Validation**
**Duration:** 4-5 hours  
**Focus:** Complex Pydantic models, nested data, and comprehensive validation

#### Learning Objectives:
- Master Pydantic Field validators
- Implement complex nested data structures
- Handle optional fields and default values
- Create custom validation logic
- Implement proper error handling with HTTPException

#### Challenge Tasks:

**Task 2.1: E-Commerce Order System**
Build an order management API with:
- Nested Pydantic models (Order contains multiple OrderItems)
- Product model with price validation (> 0)
- Quantity validation (1-100)
- Automatic total calculation
- Discount code validation (custom validator)
- Email format validation for customer
- Date validation (order date cannot be in future)

**Task 2.2: Weather Station Data Collector**
- Accept weather data with multiple sensors
- Validate temperature range (-50 to 50°C)
- Humidity percentage (0-100)
- Wind speed validation
- Implement data quality checks (reject if more than 30% of readings are missing)
- Calculate averages and trends
- Use Field() with constraints

#### Success Criteria:
- [ ] Custom validators work correctly
- [ ] Nested models validate properly
- [ ] Helpful error messages for validation failures
- [ ] Optional fields handled gracefully
- [ ] All edge cases covered

#### Claude Code Prompt for Homework 2:
```
I'm working on Homework 2 about advanced Pydantic validation and nested models.

Task: [Specify which task - E-commerce or Weather Station]
Current progress: [What you've implemented]
Challenge: [Specific validation or nesting issue]

Guide me through this like a TA:
1. Before helping with validation, ask me: "What should happen if [edge case]?"
2. If I'm stuck on nested models, ask me to draw out the data structure on paper first
3. For custom validators, have me explain the validation logic in plain English first
4. Ask me which Pydantic Field parameters I think I need and why
5. When I show you an error, ask me to read the error message carefully and hypothesize what's wrong
6. Prompt me to think about: What inputs would break my validation?
7. Instead of giving me the validator, ask: "What steps would you take to validate this?"

Help me build the mental model, not just the code.
```

---

### **Homework 3: Database Integration with SQLAlchemy**
**Duration:** 5-6 hours  
**Focus:** CRUD operations, database relationships, and session management

#### Learning Objectives:
- Implement SQLAlchemy models with relationships
- Master database session management
- Build complete CRUD operations
- Handle transactions and rollbacks
- Implement proper dependency injection

#### Challenge Tasks:

**Task 3.1: Social Media Post System**
Create a database-backed API for:
- Users table (id, username, email, created_at)
- Posts table (id, title, content, user_id, created_at)
- Comments table (id, content, post_id, user_id, created_at)
- Implement relationships (User has many Posts, Post has many Comments)
- CRUD for all entities
- Endpoint to get user with all their posts and comments (nested)
- Implement soft delete (don't actually delete, use is_deleted flag)
- Add pagination for listing endpoints

**Task 3.2: Task Management System**
- Projects table (id, name, description)
- Tasks table (id, title, status, priority, project_id, due_date)
- Many-to-many relationship: Tasks can have multiple tags
- Filter tasks by status, priority, overdue
- Move tasks between projects
- Prevent deletion of projects with active tasks

#### Success Criteria:
- [ ] Relationships work correctly
- [ ] Sessions are managed properly (no leaks)
- [ ] Transactions rollback on errors
- [ ] Pagination implemented
- [ ] Foreign key constraints respected
- [ ] Database queries are efficient (no N+1 queries)

#### Claude Code Prompt for Homework 3:
```
Working on Homework 3: Database Integration with SQLAlchemy

Task: [Social Media System or Task Management]
Current state: [What database models and endpoints you've created]
Issue: [Specific database/relationship problem]

Please guide me as a TA would:
1. Before I create relationships, ask me: "How would you describe the relationship between these entities in plain English?"
2. If I have session management issues, ask me to trace where sessions are opened and closed
3. For N+1 query problems, ask me to check how many SQL queries are executed
4. When building CRUD operations, ask: "What could go wrong at each step?" (create, read, update, delete)
5. If I'm getting foreign key errors, guide me to understand: "What is the database trying to protect?"
6. For transactions, ask me: "At what points should we commit? When should we rollback?"
7. Prompt me to use SQLAlchemy relationships instead of manual joins - why is this better?

Help me understand database concepts and SQLAlchemy patterns, not just syntax.
```

---

### **Homework 4: Async Programming & Performance**
**Duration:** 4-5 hours  
**Focus:** Asynchronous operations, concurrent requests, and performance optimization

#### Learning Objectives:
- Understand async/await patterns
- Implement async database operations
- Handle concurrent requests efficiently
- Measure and compare sync vs async performance
- Use asyncio for I/O-bound operations

#### Challenge Tasks:

**Task 4.1: Multi-API Data Aggregator**
Build an API that aggregates data from multiple sources:
- Create 3 mock external APIs (weather, news, stocks)
- Implement sync version: calls APIs sequentially
- Implement async version: calls APIs concurrently
- Compare response times
- Handle timeouts gracefully (use asyncio.timeout)
- Implement fallback if one API fails

**Task 4.2: Async Database Operations**
- Convert a sync CRUD app to async using asyncpg or asyncio-compatible ORM
- Implement async bulk insert (100+ records)
- Create endpoint that makes 5 database queries concurrently
- Measure performance difference between sync and async
- Implement connection pooling

#### Success Criteria:
- [ ] Async version is significantly faster for I/O operations
- [ ] No blocking operations in async code
- [ ] Proper error handling in async context
- [ ] Understand when to use async vs sync
- [ ] Connection pool managed correctly

#### Claude Code Prompt for Homework 4:
```
Working on Homework 4: Asynchronous Programming

Task: [Multi-API Aggregator or Async Database Operations]
What I've built: [Sync or async version and current state]
Confusion: [Specific async concept or implementation challenge]

TA-style guidance needed:
1. Before diving in, ask me: "What operations in your code are I/O bound vs CPU bound?"
2. If I'm mixing sync and async, ask me to identify which functions should be async
3. For performance comparison, guide me to add timing measurements - where should they go?
4. When I use await, ask me: "What is this code waiting for?"
5. If I have deadlocks or hangs, help me trace: "What is blocking? What is it waiting for?"
6. For concurrent operations, ask: "Should these run in parallel or sequence? Why?"
7. Prompt me to think about error handling: "If one async operation fails, what happens to the others?"

Help me build intuition about async programming, not just memorize syntax.
```

---

### **Homework 5: Authentication, Authorization & Security**
**Duration:** 5-6 hours  
**Focus:** JWT tokens, API keys, OAuth, secure password handling

#### Learning Objectives:
- Implement JWT authentication
- Create API key validation system
- Hash passwords securely (bcrypt)
- Implement role-based access control (RBAC)
- Understand OAuth2 flows
- Secure sensitive endpoints

#### Challenge Tasks:

**Task 5.1: Multi-Tenant Blog Platform**
Create a secure blogging API:
- User registration with password hashing (bcrypt)
- Login endpoint returning JWT token
- Roles: Admin, Author, Reader
- Admins can delete any post
- Authors can CRUD their own posts
- Readers can only read
- Implement token refresh mechanism
- Add rate limiting per user role

**Task 5.2: Enterprise API Gateway**
- Multiple authentication methods: JWT, API Key, Basic Auth
- Create API keys with expiration dates
- Implement permission system (read, write, admin)
- Audit log for all authenticated requests
- Endpoints for key management (create, revoke, list)
- Different rate limits based on API key tier

#### Success Criteria:
- [ ] Passwords never stored in plain text
- [ ] JWT tokens validated on protected routes
- [ ] Unauthorized access properly rejected (401, 403)
- [ ] Role-based permissions enforced
- [ ] Tokens expire correctly
- [ ] No security vulnerabilities (SQL injection, etc.)

#### Claude Code Prompt for Homework 5:
```
Working on Homework 5: Authentication & Security

Task: [Blog Platform or API Gateway]
Implementation status: [What auth mechanism you've built]
Security concern: [Specific auth/authz challenge]

Guide me like a security-focused TA:
1. Before implementing passwords, quiz me: "Why can't we store passwords as plain text?"
2. For JWT tokens, ask me to explain: "What information should/shouldn't go in a JWT payload?"
3. When implementing roles, have me map out: "Which role can do what actions?"
4. If I'm confused about 401 vs 403, ask me to explain the difference
5. For dependencies, guide me: "At what point in the request lifecycle should we validate the token?"
6. Ask me to think through attack scenarios: "What would a malicious user try to do?"
7. Prompt me to read about: "What security headers should a production API have?"

Help me think like a security engineer, not just implement features.
```

---

### **Homework 6: ML Model Serving & Serialization**
**Duration:** 4-5 hours  
**Focus:** Model deployment, pickle/joblib, input validation, batch predictions

#### Learning Objectives:
- Serialize and deserialize ML models
- Create prediction endpoints
- Validate ML input data
- Handle batch predictions
- Implement model versioning
- Add prediction caching

#### Challenge Tasks:

**Task 6.1: House Price Predictor API**
Deploy a real ML model:
- Train a regression model (sklearn) on housing data
- Serialize with joblib
- Create /predict endpoint with proper input validation
- Handle both single and batch predictions
- Add model metadata endpoint (/model/info)
- Implement basic caching for repeated inputs
- Return prediction + confidence score

**Task 6.2: Multi-Model Serving System**
- Support multiple models (v1, v2, v3)
- Client can specify model version in request
- Default to latest version
- Implement A/B testing (route 10% to new model)
- Track prediction latency per model
- Endpoint to compare predictions across versions

#### Success Criteria:
- [ ] Model loads correctly on startup
- [ ] Input data validated before prediction
- [ ] Batch predictions are efficient
- [ ] Proper error handling for invalid inputs
- [ ] Model version management works
- [ ] Response includes relevant metadata

#### Claude Code Prompt for Homework 6:
```
Working on Homework 6: ML Model Integration

Task: [House Price Predictor or Multi-Model System]
Current progress: [Model serialization, endpoints created]
Challenge: [Specific ML serving issue]

TA guidance approach:
1. Before loading models, ask me: "Where should the model loading happen? Why?"
2. For input validation, prompt me: "What could go wrong with user input? How do we prevent it?"
3. If batch predictions are slow, guide me: "How does the model.predict work? Can we optimize?"
4. For caching predictions, ask: "What makes a good cache key for ML predictions?"
5. When handling errors, explore: "What types of errors might occur during prediction?"
6. For model versioning, challenge me: "How would you ensure backward compatibility?"
7. Prompt experiments: "How would you test if the model is working correctly in the API?"

Help me think about ML systems design, not just wrapping a model in an endpoint.
```

---

### **Homework 7: Testing & Debugging**
**Duration:** 4-5 hours  
**Focus:** Unit tests, integration tests, pytest, test fixtures, debugging techniques

#### Learning Objectives:
- Write comprehensive tests with pytest
- Create test fixtures
- Mock external dependencies
- Test database operations
- Implement test coverage
- Debug FastAPI applications

#### Challenge Tasks:

**Task 7.1: Build Comprehensive Test Suite**
For an existing CRUD API (you can use one you built earlier):
- Write unit tests for all utility functions
- Integration tests for all endpoints
- Test successful cases and error cases
- Mock database operations
- Test authentication/authorization
- Achieve 80%+ code coverage
- Create fixtures for test data

**Task 7.2: Debugging Challenge**
You'll be given a buggy FastAPI application with:
- Memory leaks (database sessions not closed)
- N+1 query problems
- Race conditions in async code
- Validation that's too loose
- Security vulnerabilities

Identify and fix all issues using debugging techniques.

#### Success Criteria:
- [ ] Tests cover all endpoints
- [ ] Both success and failure cases tested
- [ ] Fixtures used appropriately
- [ ] Database tests use test database
- [ ] All tests pass
- [ ] Code coverage measured and reported
- [ ] Bugs identified and fixed with explanations

#### Claude Code Prompt for Homework 7:
```
Working on Homework 7: Testing & Debugging

Task: [Building test suite or Debugging challenge]
Current state: [Tests written or bugs found]
Struggling with: [Specific testing or debugging issue]

TA-guided learning:
1. Before writing tests, ask me: "What are all the possible outcomes of this function/endpoint?"
2. For test organization, prompt: "Which tests should be unit vs integration? Why?"
3. When creating fixtures, guide me: "What data is reused across tests? What should be isolated?"
4. If tests are flaky, ask: "What external state might affect this test?"
5. For debugging, walk me through: "What tool would help you identify this issue? (profiler, logger, debugger)"
6. When I find a bug, ask: "Why did this happen? How can we prevent it in the future?"
7. Challenge me: "How would you test this without making real API calls?"

Help me develop a testing mindset and debugging methodology.
```

---

### **Homework 8: Caching & Performance Optimization**
**Duration:** 5-6 hours  
**Focus:** Redis integration, caching strategies, query optimization, profiling

#### Learning Objectives:
- Implement Redis caching
- Understand cache invalidation strategies
- Profile and optimize slow endpoints
- Reduce database query overhead
- Implement rate limiting with Redis
- Measure performance improvements

#### Challenge Tasks:

**Task 8.1: High-Traffic News API**
Build a news aggregator with caching:
- Fetch articles from external API
- Cache articles in Redis (TTL: 5 minutes)
- Implement cache-aside pattern
- Add cache hit/miss metrics
- Implement rate limiting per user (Redis)
- Profile API before and after caching

**Task 8.2: Database Query Optimizer**
Take a slow CRUD API and optimize:
- Identify N+1 query problems
- Implement eager loading with SQLAlchemy
- Add database query result caching
- Implement pagination with cursor-based approach
- Add database indexes
- Use cProfile to measure improvements
- Document performance gains

#### Success Criteria:
- [ ] Cache hit rate > 70% for repeated requests
- [ ] Response time reduced significantly
- [ ] Redis connection pool managed properly
- [ ] Cache invalidation works correctly
- [ ] Rate limiting functions as expected
- [ ] Performance metrics documented

#### Claude Code Prompt for Homework 8:
```
Working on Homework 8: Caching & Performance Optimization

Task: [News API or Database Optimizer]
Current implementation: [Caching setup or optimization attempts]
Performance issue: [Specific bottleneck or caching problem]

Guide me systematically:
1. Before caching, ask me: "What data changes frequently? What can be cached?"
2. For cache keys, prompt: "What makes each cached item unique?"
3. When choosing TTL, guide: "How stale can this data be before it's a problem?"
4. If cache hit rate is low, investigate: "Why aren't cache keys matching?"
5. For performance profiling, direct me: "Where should you add timing measurements?"
6. When optimizing queries, ask: "How many database calls is this making? Can we reduce them?"
7. Challenge me: "How would you invalidate cache when data changes?"

Help me develop performance optimization intuition, not just use Redis.
```

---

### **Homework 9: Monitoring, Logging & Observability**
**Duration:** 5-6 hours  
**Focus:** Prometheus, Grafana, structured logging, metrics collection, alerting

#### Learning Objectives:
- Implement Prometheus metrics
- Create Grafana dashboards
- Set up structured logging
- Track custom business metrics
- Implement health check endpoints
- Understand observability principles

#### Challenge Tasks:

**Task 9.1: Observable E-commerce API**
Instrument an e-commerce API with:
- Request duration histograms (per endpoint)
- Request count metrics (by method, status)
- Custom business metrics (orders per hour, revenue)
- Structured JSON logging (with correlation IDs)
- Health and readiness endpoints
- Error rate tracking
- Set up Prometheus + Grafana with Docker

**Task 9.2: Production-Ready Monitoring**
- Implement request tracing with correlation IDs
- Log all errors with context (user, request data)
- Create 5 meaningful Grafana dashboards
- Set up alerting rules (high error rate, slow responses)
- Implement middleware for automatic logging
- Track 95th percentile response times

#### Success Criteria:
- [ ] Prometheus scrapes metrics successfully
- [ ] Grafana dashboards are informative
- [ ] Logs are structured and searchable
- [ ] Custom metrics accurately track business KPIs
- [ ] Health endpoints return correct status
- [ ] Can troubleshoot issues using logs and metrics

#### Claude Code Prompt for Homework 9:
```
Working on Homework 9: Monitoring & Observability

Task: [Observable E-commerce or Production Monitoring]
Current setup: [What metrics/logging you've implemented]
Challenge: [Specific monitoring or dashboard issue]

TA-style support:
1. Before adding metrics, ask: "What do you need to know about this API in production?"
2. For metric naming, guide: "What convention makes metrics easy to understand and query?"
3. When creating dashboards, prompt: "What questions would an operator need answered?"
4. If Prometheus isn't scraping, debug with: "Check the /metrics endpoint - what do you see?"
5. For logging, ask: "What information would help debug this issue in production?"
6. When setting alerts, challenge: "At what threshold should someone be woken up?"
7. Guide exploration: "How would you use these metrics to identify a performance regression?"

Help me think like a Site Reliability Engineer, building observable systems.
```

---

### **Homework 10: Containerization & Deployment Preparation**
**Duration:** 4-5 hours  
**Focus:** Docker, docker-compose, environment management, deployment best practices

#### Learning Objectives:
- Write efficient Dockerfiles
- Use docker-compose for multi-service apps
- Manage environment variables securely
- Implement health checks
- Optimize image size
- Understand deployment considerations

#### Challenge Tasks:

**Task 10.1: Containerize Full-Stack API**
Dockerize an API with multiple dependencies:
- Create multi-stage Dockerfile (build + production)
- Set up docker-compose with:
  - FastAPI service
  - PostgreSQL database
  - Redis cache
  - Prometheus
  - Grafana
- Use environment variables for configuration
- Implement health checks
- Create docker-compose for development and production
- Document startup process

**Task 10.2: Production-Ready Container**
- Optimize Dockerfile for minimal image size
- Implement proper signal handling (graceful shutdown)
- Use non-root user in container
- Add .dockerignore file
- Implement secrets management
- Create database migration strategy
- Document deployment process

#### Success Criteria:
- [ ] All services start with docker-compose up
- [ ] Environment variables managed securely
- [ ] Image size optimized (< 500MB if possible)
- [ ] Health checks work correctly
- [ ] Services can communicate
- [ ] Database data persists across restarts
- [ ] Logs are accessible

#### Claude Code Prompt for Homework 10:
```
Working on Homework 10: Docker & Deployment

Task: [Full-Stack API or Production Container]
Current state: [Dockerfile/docker-compose setup]
Issue: [Specific containerization or orchestration problem]

Guide me through Docker concepts:
1. Before writing Dockerfile, ask: "What are all the dependencies this app needs?"
2. For multi-stage builds, prompt: "Why separate build and production stages?"
3. When services won't connect, debug: "What network are they on? Can they reach each other?"
4. For environment variables, guide: "Which configs should change between environments?"
5. If image is large, challenge: "What's taking up space? What can we remove?"
6. For health checks, ask: "How do you know if your app is healthy vs just running?"
7. Prompt security thinking: "Why shouldn't containers run as root?"

Help me understand containerization principles, not just Docker commands.
```

---

## 🎯 MAJOR GUIDED PROJECT

### **Project: Comprehensive AI-Powered Learning Platform API**
**Duration:** 20-30 hours  
**Complexity:** Advanced - Integrates all learned concepts

#### Project Overview:
Build a production-ready API for an AI-powered educational platform that generates and serves educational content, tracks student progress, and provides personalized recommendations.

#### Core Features:

**1. User Management & Authentication (5 hours)**
- User registration, login, JWT tokens
- Role-based access (Admin, Teacher, Student)
- Profile management
- Password reset functionality

**2. Course & Content Management (6 hours)**
- CRUD for courses, lessons, quizzes
- Hierarchical content structure
- Markdown content support
- File uploads (images, PDFs)
- Versioning system

**3. AI Integration - Content Generation (5 hours)**
- Integration with LLM API (OpenAI/Anthropic)
- Generate explanations for concepts
- Create practice questions
- Code snippet generation with syntax highlighting
- Caching AI responses in Redis

**4. Progress Tracking & Analytics (4 hours)**
- Track lesson completion
- Quiz scores and attempts
- Learning streak tracking
- Time spent analytics
- Performance dashboard data endpoints

**5. Database Design (3 hours)**
- Users, Courses, Lessons, Quizzes, Questions
- Enrollments, Progress, Scores
- Relationships and constraints
- Database migrations

**6. Advanced Features (4 hours)**
- Real-time notifications (WebSocket)
- Search functionality (full-text search)
- Recommendation system (basic collaborative filtering)
- Export progress reports (PDF generation)

**7. Infrastructure (4 hours)**
- Docker containerization
- Redis for caching and rate limiting
- PostgreSQL database
- Prometheus + Grafana monitoring
- Structured logging

**8. Testing & Documentation (3 hours)**
- Comprehensive test suite
- API documentation with examples
- Deployment guide
- Performance benchmarks

#### Technical Requirements:

**Backend:**
- FastAPI with async/await
- SQLAlchemy (async) with PostgreSQL
- Pydantic for data validation
- JWT authentication
- Redis for caching

**External Integrations:**
- LLM API (OpenAI or Anthropic)
- File storage (local or S3)
- Email service (optional)

**DevOps:**
- Docker + docker-compose
- Prometheus + Grafana
- GitHub Actions (optional)

**Testing:**
- pytest with >80% coverage
- Integration tests
- Performance benchmarks

#### Architecture:

```
project/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── users.py
│   │   │   │   ├── auth.py
│   │   │   │   ├── courses.py
│   │   │   │   ├── lessons.py
│   │   │   │   ├── quizzes.py
│   │   │   │   ├── progress.py
│   │   │   │   └── ai_generate.py
│   │   │   └── api.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── dependencies.py
│   ├── db/
│   │   ├── database.py
│   │   ├── models.py
│   │   └── repositories/
│   ├── schemas/
│   │   ├── user.py
│   │   ├── course.py
│   │   └── ...
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── recommendation_service.py
│   │   └── analytics_service.py
│   ├── cache/
│   │   └── redis_cache.py
│   ├── middleware/
│   │   └── logging_middleware.py
│   └── main.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

#### Deliverables:

1. **Code Repository**
   - Well-organized code following best practices
   - Git history showing incremental development
   - Comprehensive README

2. **API Documentation**
   - Auto-generated Swagger docs
   - Postman collection
   - Usage examples

3. **Testing**
   - Test suite with good coverage
   - Test documentation
   - Performance benchmarks

4. **Deployment**
   - Docker setup working locally
   - Environment configuration guide
   - Monitoring dashboards

5. **Project Report** (2-3 pages)
   - Architecture decisions and rationale
   - Challenges faced and solutions
   - Performance optimization results
   - Future improvements

#### Evaluation Criteria:

**Functionality (30%)**
- All core features working
- Edge cases handled
- Error handling robust

**Code Quality (25%)**
- Clean, readable code
- Proper abstractions
- Following best practices
- Good project structure

**Performance (15%)**
- Efficient database queries
- Caching implemented well
- Response times acceptable
- Handles concurrent requests

**Testing (15%)**
- Good test coverage
- Tests are meaningful
- Edge cases covered

**Documentation (10%)**
- Clear README
- API docs complete
- Code comments where needed

**DevOps (5%)**
- Docker setup works
- Easy to run locally
- Monitoring configured

#### Claude Code Prompt for Major Project:
```
I'm working on the Major Project: AI-Powered Learning Platform API

Current phase: [Which feature/component you're building]
What I've completed: [List of features already implemented]
Current challenge: [Specific problem or design decision]

Please guide me through this project like a senior engineering mentor:

**For Architecture & Design:**
1. Before I implement a feature, ask me: "How will this component interact with others?"
2. Prompt me to think: "What would happen if [this scales/fails/gets attacked]?"
3. Challenge design decisions: "Why this approach vs [alternative]? What are tradeoffs?"

**For Implementation:**
1. When I'm stuck, ask me to explain the problem in simple terms first
2. Guide me to relevant docs but don't write the code
3. Ask: "What similar thing have you built? How is this different?"
4. Prompt consideration of: "What validations are needed? What can go wrong?"

**For Testing:**
1. Before writing tests, ask: "What are all the scenarios to test?"
2. Guide me: "What mocks are needed? What should be integration tested?"
3. Prompt: "How would you test this in isolation?"

**For Performance:**
1. Ask: "Where are the bottlenecks likely to be?"
2. Guide profiling: "What metrics tell you if this is fast enough?"
3. Challenge: "Could this be cached? Should it be async?"

**For Security:**
1. Regularly prompt: "What security concerns exist here?"
2. Ask: "Who should be able to access this? How do we enforce that?"
3. Guide: "What validation prevents malicious input?"

**Project Management:**
1. Help me break down large features into smaller tasks
2. Suggest which order to implement features and why
3. Remind me to commit frequently with clear messages

**Learning Opportunities:**
1. Point out when I'm reinventing the wheel - suggest libraries/patterns
2. Highlight when I've solved something elegantly - help me understand why
3. Connect current work to computer science fundamentals
4. Suggest additional challenges: "What if we needed to support [X]?"

**Code Review Style:**
1. Ask questions about my implementation choices
2. Point out potential issues without giving solutions immediately
3. Encourage me to refactor before moving on
4. Help me think about maintainability and extensibility

**When I'm Overwhelmed:**
1. Help me prioritize: "What's the MVP vs nice-to-have?"
2. Break down the problem: "Let's solve one piece at a time"
3. Remind me of similar problems I've solved before

**When I'm Confident:**
1. Introduce edge cases I haven't considered
2. Challenge me with "what if" scenarios
3. Push me to think about production readiness

Remember: Don't write code for me. Help me think through problems, understand concepts, and build solutions myself. Ask probing questions, provide conceptual guidance, and help me develop as an engineer.

If I specifically ask for complete code, remind me that the goal is learning, and provide pseudocode or high-level guidance instead.
```

---

## 📊 Progress Tracking

### Homework Completion Checklist:
- [ ] Homework 1: API Fundamentals & FastAPI Basics
- [ ] Homework 2: Advanced Routing & Data Validation
- [ ] Homework 3: Database Integration with SQLAlchemy
- [ ] Homework 4: Async Programming & Performance
- [ ] Homework 5: Authentication, Authorization & Security
- [ ] Homework 6: ML Model Serving & Serialization
- [ ] Homework 7: Testing & Debugging
- [ ] Homework 8: Caching & Performance Optimization
- [ ] Homework 9: Monitoring, Logging & Observability
- [ ] Homework 10: Containerization & Deployment Preparation

### Major Project Milestones:
- [ ] Project Setup & Architecture Design
- [ ] User Management & Authentication
- [ ] Course & Content Management
- [ ] AI Integration
- [ ] Progress Tracking & Analytics
- [ ] Advanced Features
- [ ] Infrastructure & DevOps
- [ ] Testing & Documentation
- [ ] Final Review & Deployment

---

## 💡 Learning Tips

**For Maximum Brain Engagement:**

1. **Don't Look at Solutions First** - Struggle is where learning happens
2. **Draw Diagrams** - Visualize architecture and data flow before coding
3. **Explain Out Loud** - If you can't explain it, you don't understand it
4. **Test Early and Often** - Write tests as you build, not after
5. **Use the TA Prompts** - They're designed to build understanding, not just finish tasks
6. **Iterate** - First make it work, then make it right, then make it fast
7. **Document Your Thinking** - Write comments explaining WHY, not just WHAT
8. **Take Breaks** - Your brain needs time to consolidate learning
9. **Connect Concepts** - Relate new learning to things you already know
10. **Teach Others** - Best way to solidify understanding

**When You're Stuck:**

1. Read the error message carefully (what is it really saying?)
2. Check FastAPI documentation
3. Print/log intermediate values
4. Break the problem into smaller pieces
5. Rubber duck debug (explain to an imaginary listener)
6. Use the Claude Code prompts for guidance
7. Search for similar problems (but understand solutions, don't just copy)

**Progressive Complexity:**

Each homework builds on previous concepts. If you're struggling with Homework N, make sure you truly understand Homework N-1.

---

## 🎓 Certification Criteria

You've mastered FastAPI when you can:

- [ ] Build a complete REST API from scratch without tutorials
- [ ] Explain the pros/cons of different architectural decisions
- [ ] Debug issues using logs, metrics, and profiling
- [ ] Write comprehensive tests for your APIs
- [ ] Deploy containerized applications
- [ ] Implement proper security and authentication
- [ ] Optimize for performance under load
- [ ] Monitor and troubleshoot production issues
- [ ] Integrate external services and databases
- [ ] Mentor others building FastAPI applications

---

## 📚 Additional Resources

**Official Documentation:**
- FastAPI: https://fastapi.tiangolo.com/
- Pydantic: https://docs.pydantic.dev/
- SQLAlchemy: https://docs.sqlalchemy.org/
- Redis: https://redis.io/docs/

**Testing:**
- pytest: https://docs.pytest.org/
- httpx: https://www.python-httpx.org/

**DevOps:**
- Docker: https://docs.docker.com/
- Prometheus: https://prometheus.io/docs/
- Grafana: https://grafana.com/docs/

**Best Practices:**
- 12-Factor App: https://12factor.net/
- REST API Design: https://restfulapi.net/

---

**Remember:** The goal isn't just to complete these assignments - it's to build deep understanding that will make you a confident, capable API developer. Take your time, think deeply, and use the Claude Code prompts to guide your learning journey!

Good luck! 🚀

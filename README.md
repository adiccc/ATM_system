# Banking API

A lightweight FastAPI-based banking service that provides basic account management, balance inquiries, and transaction processing.

## Overview

This API implements a simple banking system that allows users to check balances, make deposits, and withdraw funds. A key feature is its ability to automatically create accounts when they don't exist, providing a seamless onboarding experience for users.

## Technology Choices

### Server: Python + FastAPI

I chose to develop the server in Python over alternatives like Node.js, Java, or Go for several key reasons:
- **Personal Growth**: As a language I had some prior experience with, this project presented an excellent opportunity to deepen my knowledge and skills in Python within the 48-hour timeframe.
- **Development Speed**: Python enables faster development compared to Java or C#, which require more boilerplate code. With only 48 hours for completion, Python's concise syntax allowed for rapid implementation.
- **Readability for Future Maintenance**: Python's clean syntax makes the codebase more maintainable compared to the more complex syntax of TypeScript or Java, reducing the long-term technical debt.

### Client: React

The client application was developed using React instead of Angular, Vue.js or vanilla JavaScript for these decisive professional advantages:
- **Rapid Development Within 48 Hours**: React's component reusability and extensive npm library ecosystem enabled meeting the tight 48-hour deadline, which would have been challenging with Angular's steeper learning curve or Vue's smaller component ecosystem.
- **Performance Edge**: React's virtual DOM implementation offers superior performance for financial applications compared to Angular's dirty checking mechanism or vanilla JavaScript's manual DOM manipulation, especially critical for real-time transaction updates.
- **Future-Proof Architecture**: Unlike jQuery or vanilla JS solutions, React's component-based architecture ensures better maintainability and scalability as the application grows, providing better long-term value despite the short development window.
- **Superior State Management**: React's Context API and Redux options provide more robust solutions for complex financial application state compared to Vue's Vuex or Angular's services, essential for maintaining consistent transaction and account data.

### Deployment: Google Cloud

The application is deployed on Google Cloud rather than AWS, Azure, or on-premise solutions for these decisive advantages:
- **Faster Time-to-Production**: Google Cloud's Cloud Run enables containerized deployment in minutes versus hours with AWS ECS/EKS or days with on-premise solutions, critical for meeting our 48-hour project deadline.
- **Advanced Security Posture**: Google Cloud's default encryption, security scanning, and compliance controls surpass the manual configuration required in AWS or the complex security models in Azure, reducing security implementation time by several hours.

## Design Approach

### Auto-Account Creation

The primary enhancement to the original API is the implementation of auto-account creation. This feature addresses a common user experience issue in financial applications:

1. **Problem**: Users typically need to go through an explicit account creation process before they can perform any actions.
2. **Solution**: My implementation automatically creates accounts when:
   - A balance inquiry is made for a non-existent account
   - A deposit is attempted to a non-existent account

This approach optimizes the user journey by reducing friction points and allowing immediate engagement with the system.

Given the project's tight 48-hour timeline, this design approach allowed for rapid development while still delivering significant user experience improvements. The auto-account creation feature provided maximum value with minimal implementation complexity, making it an ideal solution within my time constraints.

### Design Decisions

#### 1. Conditional Account Creation

I implemented different behaviors for each endpoint:

- **Balance Inquiry**: Creates an account if it doesn't exist, returning a balance of 0
- **Deposit**: Creates an account if it doesn't exist, then completes the deposit
- **Withdrawal**: Does NOT create an account if it doesn't exist

This decision was made because:
- Checking a balance or making a deposit are natural entry points to banking services
- A withdrawal without prior knowledge of an account is a potentially suspicious activity

#### 2. Exception Handling Strategy

I use a try-except pattern to:
- Attempt the standard operation first
- Catch 404 (Not Found) exceptions specifically
- Take corrective actions only for these specific exceptions
- Pass through all other exceptions unchanged

This approach maintains the integrity of existing error handling while adding new functionality.

#### 3. Custom Response Messages

I've enhanced response messages to provide clear context when automatic actions occur:
- When an account is created during a deposit, the response indicates both events happened

#### 4. Service Layer Extension

I extended the `AccountService` class with a new `create_account` method that:
- Creates account objects with standardized initial values (balance = 0)
- Integrates with the existing database interface
- Returns consistent account objects

## API Endpoints

### Get Account Balance
```
GET /accounts/{account_number}/balance
```
Retrieves or creates an account and returns its balance.

### Withdraw Money
```
POST /accounts/{account_number}/withdraw
```
Withdraws funds from an existing account with sufficient balance.

### Deposit Money
```
POST /accounts/{account_number}/deposit
```
Deposits funds into an account, creating it if necessary.

## Challenges and Solutions

### 1. First-Time Python Server Development

**Challenge**: This was my first time developing a server in Python, requiring me to quickly learn FastAPI and Python's server patterns within the 48-hour timeline.

**Solution**: I leveraged Python's intuitive syntax and FastAPI's excellent documentation to rapidly build proficiency. By focusing on core functionality first and incrementally adding features, I was able to overcome the learning curve while still delivering a robust application.

### 2. Google Cloud Deployment Learning Curve

**Challenge**: Having never deployed to Google Cloud before, I needed to learn proper configuration, security practices, and deployment workflows.

**Solution**: I utilized Google's quickstart documentation and community resources to understand deployment best practices. By starting with a simple deployment and iteratively improving it, I was able to successfully deploy the application while gaining valuable cloud experience.

### 3. UI Design vs. Technical Learning Prioritization

**Challenge**: Despite my love for designing detailed mockups and interfaces, I had to manage my time efficiently given the 48-hour constraint and my desire to focus on new technical skills.

**Solution**: I strategically chose to implement a basic but functional UI to allocate more time to learning new technologies like Python server development and Google Cloud deployment. This prioritization allowed me to focus on skill development in areas that would provide the most professional growth while still meeting all project requirements.

### 4. Error Handling Consistency

**Challenge**: Integrating new logic while preserving existing error behavior.

**Solution**: I implemented targeted exception catching for 404 errors only, ensuring all other application logic and error handling remained intact.

### 5. Transaction Atomicity

**Challenge**: Ensuring operations that involve multiple steps (create account + make deposit) are handled atomically.

**Solution**: I handle the entire process within a single request handler to maintain operation integrity. In a production environment, this should be enhanced with database transactions.

## Full-Stack Architecture

The application follows a modern full-stack architecture:
1. **Backend**: Python FastAPI server providing RESTful endpoints
2. **Frontend**: React client application consuming the API
3. **Deployment**: Google Cloud infrastructure with CI/CD integration
4. **Database**: Managed database service for persistent storage

## Future Enhancements

1. **Transaction Logging**: Add comprehensive logging for all account creation and transaction events
2. **Database Transactions**: Implement proper transaction handling for multi-step operations
3. **Notification System**: Add notifications for automatic account creation
4. **Rate Limiting**: Implement rate limiting to prevent abuse of the automatic account creation feature
5. **Account Verification**: Add a verification step before automatically created accounts can perform certain operations
6. **Mobile Application**: Develop companion mobile applications using React Native
7. **Advanced Analytics**: Implement dashboards for account usage patterns and transaction analysis

## Getting Started

### Prerequisites
- Python 3.8+
- FastAPI
- Node.js and npm (for React client)
- Database system (as configured in your project)

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/banking-api.git

# Server Setup
cd banking-api/server
pip install -r requirements.txt
uvicorn app.main:app --reload

# Client Setup
cd ../client
npm install
npm start
```

### Example Usage
```bash
# Check balance (creates account if it doesn't exist)
curl -X GET "http://localhost:8000/accounts/12345/balance"

# Deposit funds (creates account if it doesn't exist)
curl -X POST "http://localhost:8000/accounts/12345/deposit" -H "Content-Type: application/json" -d '{"amount": 100.00}'

# Withdraw funds (account must exist)
curl -X POST "http://localhost:8000/accounts/12345/withdraw" -H "Content-Type: application/json" -d '{"amount": 50.00}'
```

## Deployment

The application is deployed on Google Cloud Platform.

- **Live Server URL**: https://my-atm-system.ew.r.appspot.com/
- **API Documentation**: https://my-atm-system.ew.r.appspot.com/docs (Interactive OpenAPI documentation)
- **GitHub Repository**: https://github.com/adiccc/ATM_system

You can visit the API documentation URL to explore the available endpoints, try out API calls directly in your browser, and learn more about request/response formats through the interactive OpenAPI interface.
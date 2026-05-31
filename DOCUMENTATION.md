# Physcult - Complete Documentation

**Sports Social Network - Culture of Living in Harmony**

Version: 1.0.0  
Last Updated: February 2026

---

# Table of Contents

1. [Project Overview](#project-overview)
2. [Quick Start](#quick-start)
3. [Installation Guide](#installation-guide)
4. [Architecture Overview](#architecture-overview)
5. [Features Overview](#features-overview)
6. [API Reference](#api-reference)
7. [Database Schema](#database-schema)
8. [WebSocket Events](#websocket-events)
9. [Group Chats Guide](#group-chats-guide)
10. [Deployment Guide](#deployment-guide)
11. [Configuration Guide](#configuration-guide)
12. [User Guide](#user-guide)

---

# Project Overview

Physcult is a comprehensive sports social network platform that combines fitness tracking, social interactions, and community building. Built with modern technologies for web and mobile platforms.

## Platforms

| Platform | Technology | Description |
|----------|------------|-------------|
| **Web Application** | React 18 + Vite + Tailwind CSS | Responsive web client |
| **Mobile App** | React Native 0.81 + Expo 54 | iOS & Android native apps |
| **Backend API** | Node.js + Express + SQLite | RESTful API server |
| **Real-time** | Socket.IO v4 | WebSocket communication |

## Project Statistics

| Component | Lines of Code | Files |
|-----------|---------------|-------|
| Mobile App (React Native) | ~19,700 | 50+ |
| Web Client (React) | ~3,800 | 20+ |
| Server (Node.js) | ~6,100 | 15+ |
| Database Tables | - | 30+ |
| API Endpoints | - | 80+ |
| Documentation | ~7,000 | 12 files |

## Key Features

| Feature | Description |
|---------|-------------|
| GPS Tracking | Real-time workout tracking with route visualization |
| Social Feed | Activity sharing with reactions and comments |
| Challenges | Group challenges and 1-on-1 duels |
| Communities | Create and join sports communities |
| Direct Messages | Real-time private messaging |
| Group Chats | Multi-user conversations with roles |
| Stories | 24-hour temporary posts |
| Goals | Personal fitness goals tracking |
| Statistics | Performance analytics and records |
| Gear Management | Track equipment and usage |
| Hashtags | Content discovery and organization |

## Tech Stack

### Frontend (Web)
- React 18, Vite, Tailwind CSS
- React Router DOM v6
- Leaflet (maps), Recharts (charts)
- Lucide React (icons)

### Frontend (Mobile)
- React Native 0.81, Expo SDK 54
- React Navigation v7
- React Native Maps, Victory Native
- Expo Location, Expo Notifications

### Backend
- Node.js, Express.js
- SQLite with better-sqlite3
- Socket.IO v4, JWT authentication
- Multer (file uploads), bcryptjs

---

# Quick Start

Get Physcult running on your machine in 5 minutes!

## Prerequisites

- Node.js (v16+)
- npm or yarn
- Expo CLI (for mobile): `npm install -g expo-cli`

## Setup Steps

### 1. Clone and Install

```bash
# Clone repository
git clone <repository-url>
cd physcult

# Install server
cd server && npm install && cd ..

# Install client (optional)
cd client && npm install && cd ..

# Install mobile (optional)
cd mobile && npm install && cd ..
```

### 2. Seed Database

```bash
cd server
npm run seed
```

**Default credentials**: alex@physcult.com / password123

### 3. Start Backend

```bash
cd server
node src/index.js
```

Server: http://localhost:3001

### 4. Start Frontend

**Web:**
```bash
cd client
npx vite --host
```

Web: http://localhost:5173

**Mobile:**
```bash
cd mobile
npm start
# Press 'i' for iOS, 'a' for Android
```

### 5. Login

- Email: alex@physcult.com
- Password: password123

## Common Issues

**Port in use:**
```bash
PORT=3002 node src/index.js
```

**Mobile can't connect:**

Update `mobile/src/constants/config.js`:
- iOS Simulator: `http://localhost:3001`
- Android Emulator: `http://10.0.2.2:3001`
- Physical device: `http://YOUR_IP:3001`

Find your IP: `ipconfig getifaddr en0` (macOS)

---

# Installation Guide

Complete installation instructions for development environment.

## Prerequisites

- **Node.js** v16 or higher
- **npm** or **yarn**
- **Git**
- **Expo CLI** (for mobile): `npm install -g expo-cli`

## Repository Structure

```
physcult/
├── server/          # Backend API (Node.js + Express)
├── client/          # Web app (React + Vite)
├── mobile/          # Mobile app (React Native + Expo)
└── docs/            # Documentation
```

## Installation Steps

### 1. Clone Repository

```bash
git clone <repository-url>
cd physcult
```

### 2. Install Dependencies

**Root (optional):**
```bash
npm install
```

**Server:**
```bash
cd server
npm install
```

**Web Client:**
```bash
cd client
npm install
```

**Mobile App:**
```bash
cd mobile
npm install
```

### 3. Database Setup

SQLite database is created automatically. To seed with sample data:

```bash
cd server
npm run seed
```

Creates:
- 5 sample users
- Multiple activities
- Sample follows, likes, comments

**Default credentials:**
- Email: alex@physcult.com
- Password: password123

### 4. Start Development Servers

**Option 1: All services (from root):**
```bash
npm run dev
```

**Option 2: Individual services:**

Backend:
```bash
cd server
node src/index.js
# Runs on http://localhost:3001
```

Web Client:
```bash
cd client
npx vite --host
# Runs on http://localhost:5173
```

Mobile App:
```bash
cd mobile
npm start
# Then press 'i' for iOS or 'a' for Android
```

## Configuration

### Backend Environment Variables

Create `.env` in `server/` (optional):

```env
PORT=3001
JWT_SECRET=your-secret-key-here
CORS_ORIGIN=*
```

### Mobile API Configuration

Update `mobile/src/constants/config.js`:

```javascript
// iOS Simulator
export const API_URL = 'http://localhost:3001';

// Android Emulator
export const API_URL = 'http://10.0.2.2:3001';

// Physical device (use your computer's IP)
export const API_URL = 'http://192.168.1.100:3001';
```

### Web Client API Configuration

Update `client/src/utils/api.js`:

```javascript
const BASE_URL = 'http://localhost:3001/api';
```

## Verify Installation

### Test Backend API

```bash
curl http://localhost:3001/health
# Should return: {"status":"ok"}
```

### Test Web Client

Open http://localhost:5173 and login with default credentials.

### Test Mobile App

Open in Expo Go and verify login screen appears.

## Troubleshooting

### Port Already in Use

```bash
PORT=3002 node src/index.js
```

### Database Issues

Delete and recreate:
```bash
cd server/src
rm physcult.db*
cd ..
npm run seed
```

### Expo Build Issues

Clear cache:
```bash
cd mobile
expo start -c
```

### Module Not Found

Reinstall dependencies:
```bash
rm -rf node_modules package-lock.json
npm install
```

## Development Tools

### Recommended VS Code Extensions

- ESLint
- Prettier
- React Native Tools
- Expo Tools
- SQLite Viewer

### Database Viewer

Use [DB Browser for SQLite](https://sqlitebrowser.org/) to view:
```
server/src/physcult.db
```

---

# Architecture Overview

System architecture and technical design of Physcult.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Clients                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Web Client  │  │ iOS App      │  │ Android App  │      │
│  │  (React)     │  │ (Expo/RN)    │  │ (Expo/RN)    │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
└─────────┼─────────────────┼──────────────────┼───────────────┘
          │    HTTP/REST    │     WebSocket    │
          ▼                 ▼                  ▼
┌─────────────────────────────────────────────────────────────┐
│                      API Gateway                             │
│              Express.js Server + Socket.IO                   │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│   SQLite Database + File Storage (Uploads) + Memory Cache   │
└─────────────────────────────────────────────────────────────┘
```

## Technology Stack

### Frontend

**Web Application:**
- Framework: React 18
- Build Tool: Vite
- Styling: Tailwind CSS
- Routing: React Router DOM v6
- Maps: Leaflet + React Leaflet
- Charts: Recharts
- Icons: Lucide React
- State: React Context API

**Mobile Application:**
- Framework: React Native 0.81
- Platform: Expo SDK 54
- Navigation: React Navigation v7
- Maps: React Native Maps
- Charts: Victory Native
- Gestures: React Native Gesture Handler
- Animations: React Native Reanimated
- State: React Context API

### Backend

- Runtime: Node.js
- Framework: Express.js
- Database: SQLite3 with better-sqlite3
- Authentication: JWT (JSON Web Tokens)
- Password Hashing: bcryptjs
- File Uploads: Multer
- Real-time: Socket.IO v4
- CORS: cors middleware

### Database

- Type: SQLite (Relational)
- ORM: Raw SQL with prepared statements
- Journal Mode: WAL (Write-Ahead Logging)
- Foreign Keys: Enabled

## Architecture Patterns

### 1. Monolithic Backend

Structure:
```
server/src/
├── db/              # Database layer
├── middleware/      # Authentication & authorization
├── routes/          # API endpoints (feature-based)
├── socket/          # WebSocket handlers
├── utils/           # Helper functions
└── index.js         # Application entry point
```

### 2. Component-Based Frontend

```
src/
├── components/      # Reusable UI components
├── pages/screens/   # Route/screen components
├── context/         # Global state management
├── utils/           # Helper functions
└── constants/       # Configuration & constants
```

### 3. RESTful API Design

- Resources as nouns (e.g., `/activities`, `/users`)
- HTTP methods for actions (GET, POST, PUT, DELETE)
- Stateless authentication with JWT
- Consistent error responses
- Pagination for lists

### 4. Realtime Communication

Socket.IO for:
- Direct messaging
- Live notifications
- Typing indicators
- Activity updates

## Data Flow

### Activity Creation Flow

```
User Input → Form → HTTP POST /api/activities
    ↓
JWT Validation → Handler → Database Insert
    ↓
PR Check → Socket.IO Broadcast (if applicable)
    ↓
Response → Update UI
```

### Authentication Flow

```
Login Request → POST /api/auth/login
    ↓
Email/Password Validation → bcrypt Compare
    ↓
Generate JWT Token → Return to Client
    ↓
Store in LocalStorage/SecureStore
    ↓
Include in Future Requests (Authorization header)
    ↓
Middleware Validates Token
```

### Real-time Messaging Flow

```
User Types → Socket.IO 'typing_start'
    ↓
Server Broadcasts → Recipient Shows Indicator
    ↓
User Sends → HTTP POST /api/messages
    ↓
Database Insert → Socket.IO 'new_message'
    ↓
Recipient Receives → UI Updates
```

## Security Architecture

### Authentication & Authorization

1. **JWT-based Authentication**
   - 7-day token expiration
   - Secure storage (LocalStorage/SecureStore)
   - Bearer token in Authorization header

2. **Password Security**
   - bcrypt hashing with salt
   - Minimum 6 characters
   - No plain text storage

3. **Authorization Middleware**
   - Role-based access (user, athlete, coach, admin)
   - Blocked user checks
   - Resource ownership verification

### API Security

1. **Rate Limiting**
   - Auth endpoints: 10 requests/minute per IP
   - Prevents brute force attacks

2. **CORS Configuration**
   - Configurable origins
   - Credentials support
   - Method restrictions

3. **Security Headers**
   - X-Content-Type-Options: nosniff
   - X-Frame-Options: DENY
   - X-XSS-Protection: 1; mode=block

4. **Input Validation**
   - SQL injection prevention (prepared statements)
   - Request body validation
   - File upload restrictions

## Database Architecture

### Key Tables

- **users**: User accounts and profiles
- **activities**: Workout activities and posts
- **follows**: Social relationships
- **reactions**: Activity engagement
- **comments**: User discussions
- **messages**: Direct messaging
- **challenges**: Competitions
- **communities**: Group functionality
- **stories**: 24-hour posts
- **gear**: Equipment tracking
- **goals**: Personal objectives

### Indexing Strategy

Strategic indexes for performance:
- User lookups
- Activity feeds (by date)
- Social graphs
- Message conversations
- Challenge participants

### Data Integrity

- Foreign key constraints
- Cascade deletes
- Unique constraints
- CHECK constraints for enums

## Performance Optimization

### Backend

- Prepared SQL statements
- Database indexes
- WAL mode for concurrency
- Batch operations

### Frontend

- Code splitting (React.lazy)
- Image optimization
- Debounced inputs
- Virtualized lists
- Memoization

### Mobile

- FlatList optimization
- Image caching
- Lazy loading
- Optimistic UI updates

---

# Features Overview

Comprehensive feature list and descriptions.

## 🏃 Activity Tracking

### GPS-Tracked Workouts

- Real-time GPS tracking
- Live metrics (distance, duration, pace)
- Route visualization on maps
- Pause/Resume functionality
- Activity types: Run, Ride, Walk, Swim, Ski
- Automatic calculations:
  - Distance (km)
  - Duration (HH:MM:SS)
  - Average pace
  - Average speed
  - Elevation gain
  - Calories burned

### Manual Activity Entry

- Gym workouts
- Yoga sessions
- Indoor training
- Custom metrics
- Photo uploads (up to 5)

### Activity Details

- Title and description with #hashtags
- Performance metrics display
- Route map visualization
- Photo gallery
- Gear association
- Personal record badges
- Social engagement (likes, reactions, comments)

## 📱 Social Features

### Activity Feed

- Personalized feed from followed users
- Like and comment
- Emoji reactions (❤️ 🔥 💪 👏)
- Share activities
- Bookmark activities
- Hashtag navigation

### User Profiles

- Personal information
- Profile photos
- Activity statistics:
  - Total workouts
  - Total distance
  - Total duration
  - Calories burned
- Training streak
- Personal records showcase
- Activity history with filtering
- Followers/Following lists

### Social Interactions

- Follow/Unfollow users
- Direct messaging
- User search and discovery
- Suggested users
- User mentions in comments

## 📸 Stories

24-hour temporary content:
- Photo and text stories
- View count tracking
- Story reactions
- Auto-deletion after 24 hours
- Story rings (unviewed indicator)
- Swipe navigation

## 💬 Messaging

Real-time private conversations:
- Real-time messaging (Socket.IO)
- Typing indicators
- Read receipts
- Photo sharing
- Message editing (before read)
- Message deletion
- Conversation hiding
- Unread count badges

## 🏆 Challenges

### Group Challenges

- Create public challenges
- Join existing challenges
- Challenge types:
  - Distance goals
  - Duration goals
  - Activity count
- Real-time leaderboard
- Progress tracking
- Time-based (weekly/monthly)
- Activity-specific

### Personal Duels

- 1-on-1 competitions
- Challenge invitations
- Accept/Decline system
- Winner determination
- Duel history

## 🎯 Goals

Personal achievement tracking:
- Set personal goals:
  - Weekly distance
  - Monthly workouts
  - Duration objectives
- Activity-specific goals
- Progress visualization
- Goal completion notifications
- Multiple active goals

## 👥 Communities

Group functionality:
- Create communities
- Join/Leave communities
- Community feed
- Community posts (channel-style)
- Post reactions and comments
- Member management
- Community avatars

## 🔍 Explore

Content discovery:
- Trending activities
- Filter by activity type
- Sort options:
  - Most recent
  - Most popular
  - Trending
- Hashtag exploration
- User discovery

## 👟 Gear Management

Equipment tracking:
- Add gear items:
  - Running shoes
  - Bicycles
  - Skis
  - Other equipment
- Associate gear with activities
- Usage statistics:
  - Total distance
  - Total activities
  - Lifespan tracking
- Retirement of old gear
- Brand and model info

## 📊 Statistics

### Personal Stats

- All-time totals
- Period analysis (week/month/year)
- Activity type breakdown
- Progress charts
- Training frequency heatmaps

### Personal Records

Track best performances:
- Longest distance by type
- Longest duration
- Fastest speed
- Most elevation gain
- Most calories burned
- PR badges on activities

### Streak Tracking

- Current training streak
- Longest streak record
- Streak calendar
- Motivation system

## 🔔 Notifications

Stay updated:
- Activity engagement (likes, comments, reactions)
- Social (new followers, mentions)
- Challenge updates
- Message alerts
- Goal achievements
- Real-time delivery (Socket.IO)
- Push notifications (mobile)
- Notification center

## 🔐 Account & Settings

### Authentication

- Email/Password registration
- Secure login (JWT)
- Session management
- Auto token refresh
- Biometric auth (mobile - Face ID/Touch ID)
- PIN code protection (mobile)

### Profile Customization

- Edit profile info
- Upload/Change avatar
- Update bio and location
- Birthday (optional)
- Privacy settings

### App Settings

- Theme (Light/Dark)
- Language (English/Russian)
- Notification preferences
- Account management
- Logout

## 🌐 Multi-language Support

- English interface
- Russian interface
- Auto language detection
- Manual language switching
- Localized date/time

## 🎨 User Interface

### Web Application

- Modern design (Tailwind CSS)
- Responsive layout
- Dark mode support
- Smooth animations
- Interactive maps (Leaflet)
- Real-time charts (Recharts)

### Mobile Application

- Native feel
- Bottom tab navigation
- Smooth gestures
- Pull-to-refresh
- Skeleton loading
- Optimized performance
- Native components

## 📱 Mobile-Specific Features

- GPS access
- Camera integration
- Photo gallery access
- Location services
- Background tracking
- Push notifications
- Offline support

## 🔒 Security Features

- Password hashing (bcrypt)
- JWT authentication
- Rate limiting
- SQL injection prevention
- XSS protection
- CORS configuration
- Secure file uploads

## 🚀 Performance Features

- Lazy loading
- Code splitting
- Image compression
- Debounced search
- Paginated lists
- Efficient database queries
- WebSocket (no polling)

## 🎯 Activity Types

1. **Running** 🏃 - Distance, pace, routes, PRs
2. **Cycling** 🚴 - Speed, elevation, routes
3. **Walking** 🚶 - Distance, duration
4. **Swimming** 🏊 - Duration, optional distance
5. **Yoga** 🧘 - Time-based sessions
6. **Gym** 💪 - Strength training
7. **Skiing** ⛷️ - Distance, elevation, speed
8. **Posts** 📝 - Social updates

## 🔄 Real-time Features

Powered by Socket.IO:
- Instant message delivery
- Live typing indicators
- Real-time notifications
- Activity feed updates
- Challenge leaderboard updates
- Story view counts

---

# API Reference

Complete REST API documentation.

## Base URL

```
http://localhost:3001/api
```

## Authentication

Include JWT token in Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

## Response Format

**Success:**
```json
{
  "data": { ... },
  "message": "Success message"
}
```

**Error:**
```json
{
  "error": "Error message"
}
```

## Rate Limiting

- Auth endpoints: 10 requests/minute per IP
- Other endpoints: No limit (configure for production)

---

## Authentication Endpoints

### POST /auth/register

Register new user.

**Public endpoint**

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "name": "John Doe",
  "birthday": "1990-05-15"
}
```

**Response:** `201 Created`
```json
{
  "token": "jwt_token",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "name": "John Doe",
    "avatar": null,
    "bio": "",
    "city": "",
    "created_at": "2026-02-22T10:00:00.000Z",
    "role": "user",
    "role_verified": 0
  }
}
```

### POST /auth/login

Login to account.

**Public endpoint**

**Request:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Response:** `200 OK`
```json
{
  "token": "jwt_token",
  "user": { ... }
}
```

### GET /auth/me

Get current user info.

**Auth required**

**Response:** `200 OK`
```json
{
  "id": 1,
  "email": "user@example.com",
  "name": "John Doe",
  "avatar": "/uploads/avatars/avatar.jpg",
  "bio": "Fitness enthusiast",
  "city": "New York",
  "total_workouts": 50,
  "total_distance": 250.5,
  "total_calories": 15000
}
```

### PUT /auth/me

Update user profile.

**Auth required**

**Request:**
```json
{
  "name": "John Doe",
  "bio": "Marathon runner",
  "city": "San Francisco"
}
```

---

## Activity Endpoints

### GET /activities/feed

Get personalized activity feed.

**Auth required**

**Query:** `?page=1`

**Response:** `200 OK`
```json
{
  "activities": [
    {
      "id": 1,
      "user_id": 2,
      "user_name": "Jane Smith",
      "user_avatar": "/uploads/avatars/jane.jpg",
      "type": "run",
      "title": "Morning Run",
      "description": "Great run! #running #fitness",
      "distance": 10.5,
      "duration": 3600,
      "elevation_gain": 150,
      "calories": 650,
      "avg_speed": 10.5,
      "avg_pace": "5:42",
      "route_data": [...],
      "photos": [...],
      "gear_id": 1,
      "gear_name": "Nike Pegasus",
      "created_at": "2026-02-22T08:00:00.000Z",
      "likes_count": 15,
      "comments_count": 3,
      "is_liked": true,
      "user_reaction": "fire",
      "reactions": {
        "like": 5,
        "fire": 4,
        "muscle": 3,
        "heart": 2,
        "clap": 1
      },
      "personal_records": ["longest_distance"],
      "is_bookmarked": false
    }
  ],
  "page": 1,
  "hasMore": true
}
```

### GET /activities/explore

Explore public activities.

**Auth required**

**Query:** `?page=1&type=run&sort=popular`

### GET /activities/:id

Get single activity.

**Auth required**

**Response:** Activity object with comments

### POST /activities

Create activity.

**Auth required**

**Request:**
```json
{
  "type": "run",
  "title": "Evening Run",
  "description": "Felt great! #running",
  "distance": 5.2,
  "duration": 1800,
  "elevation_gain": 50,
  "calories": 300,
  "avg_speed": 10.4,
  "avg_pace": "5:46",
  "route_data": [...],
  "photos": [],
  "gear_id": 1
}
```

**Response:** `201 Created`

### PUT /activities/:id

Update activity (owner only).

**Auth required**

### DELETE /activities/:id

Delete activity (owner only).

**Auth required**

### POST /activities/:id/like

Toggle like on activity.

**Auth required**

### POST /activities/:id/react

React with emoji.

**Auth required**

**Request:**
```json
{
  "emoji": "fire"
}
```

Options: like, fire, muscle, heart, clap

### DELETE /activities/:id/react

Remove reaction.

**Auth required**

### POST /activities/:id/comment

Add comment.

**Auth required**

**Request:**
```json
{
  "text": "Great workout!"
}
```

### POST /activities/:id/bookmark

Toggle bookmark.

**Auth required**

### GET /activities/bookmarked

Get bookmarked activities.

**Auth required**

### GET /activities/user/:userId

Get user's activities.

**Auth required**

### GET /activities/hashtag/:tag

Get activities by hashtag.

**Auth required**

---

## User Endpoints

### GET /users/:id

Get user profile.

**Auth required**

**Response:**
```json
{
  "id": 2,
  "name": "Jane Smith",
  "email": "jane@example.com",
  "avatar": "/uploads/avatars/jane.jpg",
  "bio": "Marathon runner",
  "city": "New York",
  "total_workouts": 100,
  "total_distance": 500.5,
  "total_calories": 30000,
  "followers_count": 50,
  "following_count": 30,
  "is_following": true
}
```

### GET /users/search

Search users.

**Auth required**

**Query:** `?q=jane`

### GET /users/suggested

Get suggested users to follow.

**Auth required**

### POST /users/:id/follow

Toggle follow.

**Auth required**

### GET /users/:id/followers

Get user's followers.

**Auth required**

### GET /users/:id/following

Get users that user follows.

**Auth required**

---

## Challenge Endpoints

### GET /challenges

Get all challenges.

**Auth required**

**Response:**
```json
{
  "challenges": [
    {
      "id": 1,
      "creator_id": 1,
      "creator_name": "John Doe",
      "title": "100km Running Challenge",
      "description": "Run 100km this month!",
      "type": "run",
      "goal_type": "distance",
      "goal_value": 100,
      "start_date": "2026-02-01",
      "end_date": "2026-02-28",
      "participants_count": 25,
      "is_joined": true,
      "current_progress": 45.5,
      "leaderboard": [...]
    }
  ]
}
```

### GET /challenges/my

Get joined challenges.

**Auth required**

### GET /challenges/:id

Get single challenge with full leaderboard.

**Auth required**

### POST /challenges

Create challenge.

**Auth required**

**Request:**
```json
{
  "title": "February Running Challenge",
  "description": "Let's run together!",
  "type": "run",
  "goal_type": "distance",
  "goal_value": 100,
  "start_date": "2026-02-01",
  "end_date": "2026-02-28"
}
```

### POST /challenges/:id/join

Toggle join challenge.

**Auth required**

### DELETE /challenges/:id

Delete challenge (creator only).

**Auth required**

---

## Message Endpoints

### GET /messages/conversations

Get conversation list.

**Auth required**

**Response:**
```json
{
  "conversations": [
    {
      "id": 1,
      "participant_id": 2,
      "participant_name": "Jane Smith",
      "participant_avatar": "/uploads/avatars/jane.jpg",
      "last_message": "See you tomorrow!",
      "last_message_at": "2026-02-22T10:00:00.000Z",
      "unread_count": 3
    }
  ]
}
```

### GET /messages/conversation/:userId

Get or create conversation.

**Auth required**

### GET /messages/:conversationId

Get messages in conversation.

**Auth required**

**Query:** `?page=1`

**Response:**
```json
{
  "messages": [
    {
      "id": 1,
      "conversation_id": 1,
      "sender_id": 2,
      "sender_name": "Jane Smith",
      "sender_avatar": "/uploads/avatars/jane.jpg",
      "text": "Hello!",
      "media_url": null,
      "read": 1,
      "edited": 0,
      "created_at": "2026-02-22T09:00:00.000Z"
    }
  ],
  "page": 1,
  "hasMore": false
}
```

### POST /messages

Send message.

**Auth required**

**Request:**
```json
{
  "conversationId": 1,
  "text": "Hello there!"
}
```

### POST /messages/with-media

Send message with photo.

**Auth required**

**Form Data:**
- conversationId
- text (optional)
- photo (file)

### PUT /messages/:id

Edit message (before read).

**Auth required**

**Request:**
```json
{
  "text": "Updated message"
}
```

### DELETE /messages/:id

Delete message (sender only).

**Auth required**

### POST /messages/:conversationId/mark-read

Mark all messages as read.

**Auth required**

### GET /messages/unread-count

Get unread count.

**Auth required**

**Response:**
```json
{
  "count": 5
}
```

---

## Notification Endpoints

### GET /notifications

Get notifications.

**Auth required**

**Query:** `?page=1`

**Response:**
```json
{
  "notifications": [
    {
      "id": 1,
      "user_id": 1,
      "actor_id": 2,
      "actor_name": "Jane Smith",
      "actor_avatar": "/uploads/avatars/jane.jpg",
      "type": "like",
      "entity_type": "activity",
      "entity_id": 5,
      "text": "Jane Smith liked your activity",
      "read": 0,
      "created_at": "2026-02-22T10:00:00.000Z"
    }
  ],
  "page": 1,
  "hasMore": false
}
```

### POST /notifications/mark-all-read

Mark all as read.

**Auth required**

### GET /notifications/unread-count

Get unread count.

**Auth required**

---

## Stats Endpoints

### GET /stats/overview

Get user statistics.

**Auth required**

**Query:** `?period=week` (week/month/year/all)

**Response:**
```json
{
  "total_workouts": 100,
  "total_distance": 500.5,
  "total_duration": 180000,
  "total_calories": 30000,
  "by_type": {
    "run": {
      "count": 60,
      "distance": 400.0,
      "duration": 120000
    }
  }
}
```

### GET /stats/streak

Get training streak.

**Auth required**

**Response:**
```json
{
  "current_streak": 15,
  "longest_streak": 30,
  "last_workout_date": "2026-02-22"
}
```

### GET /stats/personal-records

Get personal records.

**Auth required**

---

## Story Endpoints

### GET /stories

Get stories from followed users.

**Auth required**

**Response:**
```json
{
  "stories": [
    {
      "user_id": 2,
      "user_name": "Jane Smith",
      "user_avatar": "/uploads/avatars/jane.jpg",
      "stories": [
        {
          "id": 1,
          "user_id": 2,
          "image_url": "/uploads/stories/story1.jpg",
          "text_content": "Great morning!",
          "bg_color": "#FF6B2B",
          "created_at": "2026-02-22T08:00:00.000Z",
          "views_count": 25,
          "has_viewed": false,
          "reactions": {
            "fire": 5,
            "heart": 3
          },
          "user_reaction": null
        }
      ]
    }
  ]
}
```

### POST /stories

Create story.

**Auth required**

**Request:**
```json
{
  "image_url": "/uploads/stories/image.jpg",
  "text_content": "Hello world!",
  "bg_color": "#FF6B2B"
}
```

### POST /stories/:id/view

Mark story as viewed.

**Auth required**

### POST /stories/:id/react

React to story.

**Auth required**

**Request:**
```json
{
  "emoji": "fire"
}
```

### DELETE /stories/:id

Delete story (owner only).

**Auth required**

---

## Goal Endpoints

### GET /goals

Get user's goals.

**Auth required**

**Response:**
```json
{
  "goals": [
    {
      "id": 1,
      "user_id": 1,
      "type": "distance",
      "activity_type": "run",
      "period": "monthly",
      "target_value": 100,
      "current_progress": 45.5,
      "active": 1,
      "created_at": "2026-02-01T00:00:00.000Z"
    }
  ]
}
```

### POST /goals

Create goal.

**Auth required**

**Request:**
```json
{
  "type": "distance",
  "activity_type": "run",
  "period": "monthly",
  "target_value": 100
}
```

### DELETE /goals/:id

Delete goal.

**Auth required**

---

## Gear Endpoints

### GET /gear

Get user's gear.

**Auth required**

**Response:**
```json
{
  "gear": [
    {
      "id": 1,
      "user_id": 1,
      "name": "Nike Pegasus 39",
      "type": "shoes",
      "brand": "Nike",
      "total_distance": 250.5,
      "total_activities": 50,
      "active": 1,
      "created_at": "2026-01-01T00:00:00.000Z"
    }
  ]
}
```

### POST /gear

Add gear.

**Auth required**

**Request:**
```json
{
  "name": "Trek Domane SL7",
  "type": "bike",
  "brand": "Trek"
}
```

### PUT /gear/:id

Update gear.

**Auth required**

### DELETE /gear/:id

Delete gear.

**Auth required**

---

## Community Endpoints

### GET /communities

Get all communities.

**Auth required**

**Response:**
```json
{
  "communities": [
    {
      "id": 1,
      "name": "NYC Runners",
      "description": "Running club in NYC",
      "avatar": "/uploads/community_avatars/nyc.jpg",
      "creator_id": 1,
      "created_at": "2026-01-01T00:00:00.000Z",
      "members_count": 150,
      "is_member": true
    }
  ]
}
```

### GET /communities/:id

Get community with posts.

**Auth required**

### POST /communities

Create community.

**Auth required**

**Request:**
```json
{
  "name": "Boston Cyclists",
  "description": "Cycling in Boston"
}
```

### POST /communities/:id/join

Toggle join community.

**Auth required**

### DELETE /communities/:id

Delete community (creator only).

**Auth required**

---

## Upload Endpoints

### POST /uploads/avatar

Upload avatar.

**Auth required**

**Form Data:**
- avatar (image file)

**Response:**
```json
{
  "avatar": "/uploads/avatars/user1_1709123456.jpg"
}
```

### POST /uploads/activity-photos

Upload activity photos.

**Auth required**

**Form Data:**
- activityId
- photos (max 5 files)

**Response:**
```json
{
  "photos": [
    "/uploads/activities/activity1_photo1.jpg",
    "/uploads/activities/activity1_photo2.jpg"
  ]
}
```

### POST /uploads/community-avatar

Upload community avatar.

**Auth required**

---

## Hashtag Endpoints

### GET /hashtags/trending

Get trending hashtags.

**Auth required**

**Response:**
```json
{
  "hashtags": [
    {
      "tag": "running",
      "usage_count": 150
    },
    {
      "tag": "fitness",
      "usage_count": 120
    }
  ]
}
```

---

## Push Notification Endpoints

### POST /push/register

Register push token.

**Auth required**

**Request:**
```json
{
  "pushToken": "ExponentPushToken[xxx]"
}
```

### DELETE /push/unregister

Unregister push notifications.

**Auth required**

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request - Invalid input |
| 401 | Unauthorized - Invalid/missing token |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource doesn't exist |
| 429 | Too Many Requests - Rate limit |
| 500 | Internal Server Error |

---

# Database Schema

Complete database structure documentation.

## Database Configuration

**Type:** SQLite  
**Journal Mode:** WAL (Write-Ahead Logging)  
**Foreign Keys:** Enabled

```sql
PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;
```

## Tables

### users

User accounts and profiles.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | User ID |
| email | TEXT | UNIQUE, NOT NULL | Email address |
| password | TEXT | NOT NULL | Hashed password |
| name | TEXT | NOT NULL | Display name |
| avatar | TEXT | DEFAULT NULL | Avatar path |
| bio | TEXT | DEFAULT '' | Biography |
| city | TEXT | DEFAULT '' | Location |
| role | TEXT | DEFAULT 'user' | Role (user/athlete/coach/admin) |
| role_verified | INTEGER | DEFAULT 0 | Verification status |
| sport_type | TEXT | DEFAULT NULL | Primary sport |
| sport_position | TEXT | DEFAULT NULL | Position/specialty |
| sport_rank | TEXT | DEFAULT NULL | Rank/level |
| status | TEXT | DEFAULT NULL | Account status |
| push_token | TEXT | DEFAULT NULL | Push notification token |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Registration date |

**Indexes:** idx_users_role

---

### activities

Workout activities and posts.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Activity ID |
| user_id | INTEGER | NOT NULL, FK → users | Owner |
| type | TEXT | NOT NULL, CHECK | Activity type |
| title | TEXT | NOT NULL | Activity title |
| description | TEXT | DEFAULT '' | Description |
| distance | REAL | DEFAULT 0 | Distance (km) |
| duration | INTEGER | DEFAULT 0 | Duration (seconds) |
| elevation_gain | REAL | DEFAULT 0 | Elevation (m) |
| calories | INTEGER | DEFAULT 0 | Calories burned |
| avg_speed | REAL | DEFAULT 0 | Average speed (km/h) |
| avg_pace | TEXT | DEFAULT '' | Average pace (mm:ss/km) |
| route_data | TEXT | DEFAULT '[]' | GPS route JSON |
| photos | TEXT | DEFAULT '[]' | Photo URLs JSON |
| gear_id | INTEGER | DEFAULT NULL, FK → gear | Associated gear |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Created date |

**CHECK:** type IN ('run','ride','walk','swim','yoga','gym','ski','post')

**Indexes:**
- idx_activities_user (user_id)
- idx_activities_created (created_at DESC)

---

### follows

Follower relationships.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Relationship ID |
| follower_id | INTEGER | NOT NULL, FK → users | Follower |
| following_id | INTEGER | NOT NULL, FK → users | Following |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Follow date |

**UNIQUE:** (follower_id, following_id)

**Indexes:**
- idx_follows_follower
- idx_follows_following

---

### reactions

Emoji reactions to activities.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Reaction ID |
| user_id | INTEGER | NOT NULL, FK → users | User |
| activity_id | INTEGER | NOT NULL, FK → activities | Activity |
| emoji | TEXT | NOT NULL, CHECK | Emoji type |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Reaction date |

**CHECK:** emoji IN ('like','fire','muscle','heart','clap')

**UNIQUE:** (user_id, activity_id)

**Indexes:** idx_reactions_activity

---

### comments

Activity comments.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Comment ID |
| user_id | INTEGER | NOT NULL, FK → users | Author |
| activity_id | INTEGER | NOT NULL, FK → activities | Activity |
| text | TEXT | NOT NULL | Comment text |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Comment date |

**Indexes:** idx_comments_activity

---

### bookmarks

Saved activities.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Bookmark ID |
| user_id | INTEGER | NOT NULL, FK → users | User |
| activity_id | INTEGER | NOT NULL, FK → activities | Activity |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Saved date |

**UNIQUE:** (user_id, activity_id)

**Indexes:** idx_bookmarks_user

---

### personal_records

Personal best achievements.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | PR ID |
| user_id | INTEGER | NOT NULL, FK → users | User |
| type | TEXT | NOT NULL | Activity type |
| category | TEXT | NOT NULL | Record category |
| value | REAL | NOT NULL | Record value |
| activity_id | INTEGER | NOT NULL, FK → activities | Activity |
| achieved_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Achievement date |

**UNIQUE:** (user_id, type, category)

**Categories:**
- longest_distance
- longest_duration
- most_calories
- most_elevation
- fastest_speed

**Indexes:** idx_pr_user

---

### goals

User fitness goals.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Goal ID |
| user_id | INTEGER | NOT NULL, FK → users | User |
| type | TEXT | NOT NULL, CHECK | Goal type |
| activity_type | TEXT | DEFAULT NULL | Activity type |
| period | TEXT | NOT NULL, CHECK | Period |
| target_value | REAL | NOT NULL | Target |
| active | INTEGER | DEFAULT 1 | Active status |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Created date |

**CHECK:**
- type IN ('distance','duration','count')
- period IN ('weekly','monthly')

**Indexes:** idx_goals_user

---

### challenges

Fitness challenges.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Challenge ID |
| creator_id | INTEGER | NOT NULL, FK → users | Creator |
| title | TEXT | NOT NULL | Title |
| description | TEXT | DEFAULT '' | Description |
| type | TEXT | NOT NULL, CHECK | Activity type |
| goal_type | TEXT | NOT NULL, CHECK | Goal type |
| goal_value | REAL | NOT NULL | Target value |
| start_date | DATE | NOT NULL | Start date |
| end_date | DATE | NOT NULL | End date |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Created date |

**CHECK:**
- type IN ('run','ride','walk','swim','yoga','gym','ski')
- goal_type IN ('distance','duration','count')

**Indexes:** idx_challenges_dates

---

### challenge_participants

Challenge participation.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Participation ID |
| challenge_id | INTEGER | NOT NULL, FK → challenges | Challenge |
| user_id | INTEGER | NOT NULL, FK → users | Participant |
| current_progress | REAL | DEFAULT 0 | Progress |
| completed | INTEGER | DEFAULT 0 | Completed |
| joined_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Join date |

**UNIQUE:** (challenge_id, user_id)

**Indexes:** idx_challenge_participants_challenge

---

### conversations

Message conversations.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Conversation ID |
| participant1_id | INTEGER | NOT NULL, FK → users | Participant 1 |
| participant2_id | INTEGER | NOT NULL, FK → users | Participant 2 |
| last_message_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Last message |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Created date |

**UNIQUE:** (participant1_id, participant2_id)

**CHECK:** participant1_id < participant2_id

**Indexes:**
- idx_conversations_p1
- idx_conversations_p2

---

### messages

Direct messages.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Message ID |
| conversation_id | INTEGER | NOT NULL, FK → conversations | Conversation |
| sender_id | INTEGER | NOT NULL, FK → users | Sender |
| text | TEXT | NOT NULL | Message text |
| media_url | TEXT | DEFAULT NULL | Media URL |
| read | INTEGER | DEFAULT 0 | Read status |
| edited | INTEGER | DEFAULT 0 | Edited status |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Send date |

**Indexes:** idx_messages_conversation

---

### notifications

User notifications.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Notification ID |
| user_id | INTEGER | NOT NULL, FK → users | Recipient |
| actor_id | INTEGER | FK → users | Actor |
| type | TEXT | NOT NULL, CHECK | Type |
| entity_type | TEXT | | Entity type |
| entity_id | INTEGER | | Entity ID |
| text | TEXT | NOT NULL | Notification text |
| read | INTEGER | DEFAULT 0 | Read status |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Created date |

**CHECK:** type IN ('like','comment','follow','challenge','message')

**Indexes:** idx_notifications_user

---

### stories

24-hour temporary posts.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Story ID |
| user_id | INTEGER | NOT NULL, FK → users | Creator |
| image_url | TEXT | | Image URL |
| text_content | TEXT | DEFAULT '' | Text overlay |
| bg_color | TEXT | DEFAULT '#000' | Background color |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Created date |

**Indexes:**
- idx_stories_user
- idx_stories_created

---

### story_views

Story view tracking.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| story_id | INTEGER | NOT NULL, FK → stories | Story |
| user_id | INTEGER | NOT NULL, FK → users | Viewer |
| viewed_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | View date |

**PK:** (story_id, user_id)

---

### communities

Community groups.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Community ID |
| name | TEXT | NOT NULL | Name |
| description | TEXT | DEFAULT '' | Description |
| avatar | TEXT | DEFAULT NULL | Avatar |
| creator_id | INTEGER | NOT NULL, FK → users | Creator |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Created date |

**Indexes:** idx_communities_creator

---

### community_members

Community membership.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| community_id | INTEGER | NOT NULL, FK → communities | Community |
| user_id | INTEGER | NOT NULL, FK → users | Member |
| joined_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Join date |

**PK:** (community_id, user_id)

---

### gear

User equipment.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Gear ID |
| user_id | INTEGER | NOT NULL, FK → users | Owner |
| name | TEXT | NOT NULL | Name |
| type | TEXT | NOT NULL, CHECK | Type |
| brand | TEXT | DEFAULT '' | Brand |
| total_distance | REAL | DEFAULT 0 | Total distance |
| total_activities | INTEGER | DEFAULT 0 | Activity count |
| active | INTEGER | DEFAULT 1 | Active status |
| created_at | DATETIME | DEFAULT CURRENT_TIMESTAMP | Created date |

**CHECK:** type IN ('shoes','bike','skis','other')

**Indexes:** idx_gear_user

---

### hashtags

Hashtag information.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PK AUTOINCREMENT | Hashtag ID |
| tag | TEXT | UNIQUE, NOT NULL | Hashtag text |
| usage_count | INTEGER | DEFAULT 0 | Usage count |

**Indexes:**
- idx_hashtags_tag
- idx_hashtags_usage

---

### activity_hashtags

Activity-hashtag relationships.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| activity_id | INTEGER | NOT NULL, FK → activities | Activity |
| hashtag_id | INTEGER | NOT NULL, FK → hashtags | Hashtag |

**PK:** (activity_id, hashtag_id)

---

## Entity Relationships

```
users (1) ----< (N) activities
users (1) ----< (N) follows (follower)
users (1) ----< (N) follows (following)
users (1) ----< (N) reactions
users (1) ----< (N) comments
users (1) ----< (N) bookmarks
users (1) ----< (N) personal_records
users (1) ----< (N) goals
users (1) ----< (N) challenges
users (1) ----< (N) challenge_participants
users (1) ----< (N) messages
users (1) ----< (N) notifications
users (1) ----< (N) stories
users (1) ----< (N) communities
users (1) ----< (N) community_members
users (1) ----< (N) gear

activities (1) ----< (N) reactions
activities (1) ----< (N) comments
activities (1) ----< (N) bookmarks
activities (1) ----< (N) activity_hashtags
activities (N) >---- (1) gear

challenges (1) ----< (N) challenge_participants
conversations (1) ----< (N) messages
communities (1) ----< (N) community_members

stories (1) ----< (N) story_views

hashtags (1) ----< (N) activity_hashtags
```

---

# WebSocket Events

Real-time communication with Socket.IO.

## Connection

### Server URL

```javascript
const SOCKET_URL = 'http://localhost:3001';
```

### Authentication

```javascript
import { io } from 'socket.io-client';

const socket = io(SOCKET_URL, {
  auth: { token: 'your_jwt_token' },
  transports: ['websocket'],
  reconnection: true,
  reconnectionDelay: 2000
});
```

### Connection Events

**connect:**
```javascript
socket.on('connect', () => {
  console.log('Connected:', socket.id);
});
```

Server auto-joins user to room: `user_${userId}`

**disconnect:**
```javascript
socket.on('disconnect', (reason) => {
  console.log('Disconnected:', reason);
});
```

**connect_error:**
```javascript
socket.on('connect_error', (error) => {
  console.error('Error:', error.message);
});
```

---

## Messaging Events

### Client → Server

**join_conversation:**
```javascript
socket.emit('join_conversation', {
  conversationId: 123
});
```

Joins room `conv_${conversationId}` to receive messages.

**leave_conversation:**
```javascript
socket.emit('leave_conversation', {
  conversationId: 123
});
```

Leaves conversation room.

**typing_start:**
```javascript
socket.emit('typing_start', {
  conversationId: 123
});
```

Notify that user is typing (throttle to max once per 2-3 seconds).

**typing_stop:**
```javascript
socket.emit('typing_stop', {
  conversationId: 123
});
```

Notify that user stopped typing.

---

### Server → Client

**new_message:**
```javascript
socket.on('new_message', (message) => {
  console.log('New message:', message);
  // Update UI
});
```

Payload:
```json
{
  "id": 456,
  "conversation_id": 123,
  "sender_id": 2,
  "sender_name": "Jane Smith",
  "sender_avatar": "/uploads/avatars/jane.jpg",
  "text": "Hello there!",
  "media_url": null,
  "read": 0,
  "edited": 0,
  "created_at": "2026-02-22T10:30:00.000Z"
}
```

**message_deleted:**
```javascript
socket.on('message_deleted', (data) => {
  console.log('Deleted:', data);
  // Remove from UI
});
```

Payload:
```json
{
  "id": 456,
  "conversation_id": 123
}
```

**message_edited:**
```javascript
socket.on('message_edited', (message) => {
  console.log('Edited:', message);
  // Update in UI
});
```

Payload: Updated message object with `edited: 1`

**user_typing:**
```javascript
socket.on('user_typing', (data) => {
  console.log('User typing:', data);
  // Show typing indicator
});
```

Payload:
```json
{
  "userId": 2,
  "conversationId": 123
}
```

**user_stop_typing:**
```javascript
socket.on('user_stop_typing', (data) => {
  // Hide typing indicator
});
```

---

## Notification Events

**new_notification:**
```javascript
socket.on('new_notification', (notification) => {
  console.log('Notification:', notification);
  // Show badge/toast
});
```

Payload:
```json
{
  "id": 789,
  "user_id": 1,
  "actor_id": 2,
  "actor_name": "Jane Smith",
  "actor_avatar": "/uploads/avatars/jane.jpg",
  "type": "like",
  "entity_type": "activity",
  "entity_id": 15,
  "text": "Jane Smith liked your activity",
  "read": 0,
  "created_at": "2026-02-22T10:35:00.000Z"
}
```

Notification types:
- `like` - Activity liked
- `comment` - Activity commented
- `follow` - New follower
- `challenge` - Challenge invitation/update
- `message` - New direct message

---

## Implementation Example

### React Native

```javascript
import { useEffect, useState } from 'react';
import { getSocket } from './utils/socket';

function ChatScreen({ route }) {
  const { conversationId } = route.params;
  const socket = getSocket();
  const [messages, setMessages] = useState([]);
  const [isTyping, setIsTyping] = useState(false);
  
  useEffect(() => {
    if (!socket) return;
    
    // Join conversation
    socket.emit('join_conversation', { conversationId });
    
    // Listen for messages
    const handleNewMessage = (msg) => {
      if (String(msg.conversation_id) === String(conversationId)) {
        setMessages(prev => [...prev, msg]);
      }
    };
    socket.on('new_message', handleNewMessage);
    
    // Listen for typing
    const handleTyping = () => {
      setIsTyping(true);
      setTimeout(() => setIsTyping(false), 3000);
    };
    socket.on('user_typing', handleTyping);
    
    // Cleanup
    return () => {
      socket.off('new_message', handleNewMessage);
      socket.off('user_typing', handleTyping);
      socket.emit('leave_conversation', { conversationId });
    };
  }, [socket, conversationId]);
  
  const handleTyping = () => {
    socket.emit('typing_start', { conversationId });
  };
  
  // ... rest of component
}
```

---

## Best Practices

### 1. Connection Management

- Single connection per app
- Enable auto-reconnection
- Disconnect on logout

### 2. Room Management

- Join rooms on mount
- Leave rooms on unmount
- Clean up listeners

### 3. Typing Indicators

- Throttle emission (max once per 2-3s)
- Auto-hide after 3-5s
- Clear on send

### 4. Error Handling

```javascript
socket.on('error', (error) => {
  console.error('Socket error:', error);
});

socket.on('connect_error', (error) => {
  console.error('Connection failed:', error);
});
```

### 5. Optimistic Updates

Update UI immediately, sync with socket events:

```javascript
const sendMessage = async (text) => {
  // Add to UI immediately
  const tempMsg = {
    id: 'temp-' + Date.now(),
    text,
    sender_id: currentUser.id,
    created_at: new Date().toISOString()
  };
  setMessages(prev => [...prev, tempMsg]);
  
  try {
    // Send to server
    const response = await api.sendMessage(conversationId, text);
    // Replace temp with real
    setMessages(prev => 
      prev.map(m => m.id === tempMsg.id ? response : m)
    );
  } catch (error) {
    // Remove failed message
    setMessages(prev => prev.filter(m => m.id !== tempMsg.id));
  }
};
```

---

## Security

### Authentication

- All connections require valid JWT
- Server validates token on connect
- Invalid tokens rejected

### Authorization

- Users only receive messages in their rooms
- Conversation access verified server-side
- Cannot join unauthorized conversations

---

## Debugging

### Enable Debug Mode

```javascript
// Client-side
localStorage.debug = 'socket.io-client:*';
```

### Monitor Events

```javascript
// Log all events
socket.onAny((eventName, ...args) => {
  console.log(`Event: ${eventName}`, args);
});
```

### Check Status

```javascript
console.log('Connected:', socket.connected);
console.log('Socket ID:', socket.id);
```

---

# Group Chats Guide

Complete guide for implementing and using group chat functionality.

## Overview

Group chats allow multiple users to communicate in a single conversation. Each group has:
- A creator (admin)
- Multiple participants with roles (admin/member)
- Group name and optional avatar
- Shared message history

## Database Schema

### conversations table (updated for groups)

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Conversation ID |
| is_group | INTEGER | 0=private, 1=group |
| group_name | TEXT | Group name |
| group_avatar | TEXT | Avatar URL |
| creator_id | INTEGER | Creator user ID |

### group_participants table

| Column | Type | Description |
|--------|------|-------------|
| conversation_id | INTEGER | Group ID |
| user_id | INTEGER | Participant ID |
| role | TEXT | 'admin' or 'member' |
| joined_at | DATETIME | Join timestamp |

## API Endpoints

### Create Group
```
POST /api/group-chats/create
Body: { name: "Team Runners", participantIds: [2, 3, 4] }
```

### Get Group Details
```
GET /api/group-chats/:id
```

### Update Group (admin only)
```
PUT /api/group-chats/:id
Body: { name: "New Name" }
```

### Upload Group Avatar (admin only)
```
POST /api/group-chats/:id/avatar
Form-Data: avatar (image file, max 5MB)
```

### Add Participants (admin only)
```
POST /api/group-chats/:id/participants
Body: { userIds: [5, 6] }
```

### Remove Participant
```
DELETE /api/group-chats/:id/participants/:userId
```

### Leave Group
```
POST /api/group-chats/:id/leave
```

### Delete Group (creator only)
```
DELETE /api/group-chats/:id
```

## WebSocket Events

### Client Receives
- `group_created` - Added to new group
- `group_updated` - Group info changed
- `participants_added` - New members added
- `participant_removed` - Member removed
- `participant_left` - Member left
- `added_to_group` - You were added
- `removed_from_group` - You were removed
- `group_deleted` - Group was deleted

### Example Implementation
```javascript
// Create group
const group = await api.post('/group-chats/create', {
  name: 'Running Club',
  participantIds: [2, 3, 4]
});

// Listen for group events
socket.on('group_created', (group) => {
  setConversations(prev => [group, ...prev]);
});

socket.on('added_to_group', (group) => {
  setConversations(prev => [group, ...prev]);
  showNotification(`Added to ${group.name}`);
});
```

## Roles and Permissions

| Action | Admin | Member |
|--------|-------|--------|
| Send messages | Yes | Yes |
| Update group name/avatar | Yes | No |
| Add participants | Yes | No |
| Remove others | Yes | No |
| Remove self | Yes | Yes |
| Leave group | No* | Yes |
| Delete group | Creator only | No |

*Creator cannot leave, only delete

---

# Deployment Guide

Production deployment instructions.

## Backend Deployment

### Prerequisites

- Node.js 16+
- Domain name configured
- SSL certificate
- Firewall configured

### Environment Setup

Create `.env` in `server/`:

```env
NODE_ENV=production
PORT=3001
JWT_SECRET=your-super-secret-key-64-chars-minimum
CORS_ORIGIN=https://yourdomain.com
DB_PATH=/var/lib/physcult/physcult.db
UPLOAD_PATH=/var/lib/physcult/uploads
```

**Generate JWT secret:**
```bash
node -e "console.log(require('crypto').randomBytes(64).toString('hex'))"
```

### VPS Deployment

**1. Install Node.js:**
```bash
sudo apt update && sudo apt upgrade -y
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs
```

**2. Setup Application:**
```bash
sudo mkdir -p /var/www/physcult
sudo chown $USER:$USER /var/www/physcult
cd /var/www/physcult
git clone <repository-url> .
cd server
npm install --production
sudo mkdir -p /var/lib/physcult/uploads
sudo chown $USER:$USER /var/lib/physcult
```

**3. Setup PM2:**
```bash
sudo npm install -g pm2
cd /var/www/physcult/server
pm2 start src/index.js --name physcult-api
pm2 startup systemd
pm2 save
```

**4. Setup Nginx:**
```bash
sudo apt install -y nginx
sudo nano /etc/nginx/sites-available/physcult
```

Configuration:
```nginx
server {
    listen 80;
    server_name api.yourdomain.com;
    client_max_body_size 10M;

    location / {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_cache_bypass $http_upgrade;
    }

    location /socket.io/ {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    location /uploads/ {
        alias /var/lib/physcult/uploads/;
        expires 7d;
        add_header Cache-Control "public, immutable";
    }
}
```

Enable:
```bash
sudo ln -s /etc/nginx/sites-available/physcult /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

**5. Setup SSL:**
```bash
sudo apt install -y certbot python3-certbot-nginx
sudo certbot --nginx -d api.yourdomain.com
```

**6. Firewall:**
```bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

### Docker Deployment

**Dockerfile:**
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY server/package*.json ./
RUN npm ci --production
COPY server/ .
RUN mkdir -p /data/uploads
EXPOSE 3001
CMD ["node", "src/index.js"]
```

**docker-compose.yml:**
```yaml
version: '3.8'
services:
  api:
    build: .
    ports:
      - "3001:3001"
    environment:
      - NODE_ENV=production
      - JWT_SECRET=${JWT_SECRET}
    volumes:
      - physcult-data:/data
    restart: unless-stopped
volumes:
  physcult-data:
```

Deploy:
```bash
docker-compose up -d
```

---

## Web Client Deployment

### Build

```bash
cd client
npm install
npm run build
```

Output: `client/dist/`

### Static Hosting (Netlify)

Create `netlify.toml`:
```toml
[build]
  command = "npm run build"
  publish = "dist"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
```

Deploy:
```bash
npm install -g netlify-cli
netlify deploy --prod
```

### Nginx Static Hosting

```bash
sudo cp -r client/dist/* /var/www/physcult-web/
```

Nginx config:
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    root /var/www/physcult-web;
    index index.html;

    gzip on;
    gzip_types text/plain text/css application/json application/javascript;

    location ~* \.(js|css|png|jpg|jpeg|gif|svg)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

---

## Mobile App Deployment

### Prerequisites

- Expo account
- Apple Developer account (iOS)
- Google Play Developer account (Android)

### Configuration

Update `mobile/app.json`:
```json
{
  "expo": {
    "name": "Physcult",
    "version": "1.0.0",
    "ios": {
      "bundleIdentifier": "com.yourcompany.physcult"
    },
    "android": {
      "package": "com.yourcompany.physcult"
    },
    "extra": {
      "apiUrl": "https://api.yourdomain.com"
    }
  }
}
```

### Build with EAS

```bash
npm install -g eas-cli
eas login
cd mobile
eas build:configure

# Android
eas build --platform android --profile production

# iOS
eas build --platform ios --profile production

# Submit
eas submit --platform android
eas submit --platform ios
```

---

## Database Management

### Backup Script

Create `/usr/local/bin/backup-physcult.sh`:
```bash
#!/bin/bash
BACKUP_DIR="/var/backups/physcult"
DB_PATH="/var/lib/physcult/physcult.db"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR
sqlite3 $DB_PATH ".backup '$BACKUP_DIR/physcult_$DATE.db'"
tar -czf $BACKUP_DIR/uploads_$DATE.tar.gz /var/lib/physcult/uploads/
find $BACKUP_DIR -name "physcult_*.db" -mtime +30 -delete
echo "Backup completed: $DATE"
```

Schedule:
```bash
sudo chmod +x /usr/local/bin/backup-physcult.sh
sudo crontab -e
# Add: 0 2 * * * /usr/local/bin/backup-physcult.sh
```

---

## Monitoring

### Health Checks

```bash
curl https://api.yourdomain.com/health
pm2 status
pm2 logs physcult-api
pm2 monit
```

### Log Rotation

Create `/etc/logrotate.d/physcult`:
```
/var/log/physcult/*.log {
    daily
    rotate 14
    compress
    notifempty
    postrotate
        pm2 reloadLogs
    endscript
}
```

---

## Security Checklist

- [ ] Change default JWT secret
- [ ] Enable HTTPS/SSL
- [ ] Configure firewall
- [ ] Regular security updates
- [ ] Strong SSH passwords
- [ ] Setup fail2ban
- [ ] Regular database backups
- [ ] Monitor logs
- [ ] Keep dependencies updated
- [ ] Configure rate limiting
- [ ] Use environment variables for secrets

---

# Configuration Guide

Environment variables and settings.

## Backend Configuration

### Environment Variables

```env
# Server
NODE_ENV=production
PORT=3001
HOST=0.0.0.0

# Security
JWT_SECRET=your-secret-key-64-chars
JWT_EXPIRES_IN=7d

# CORS
CORS_ORIGIN=https://yourdomain.com

# Database
DB_PATH=./src/physcult.db
DB_JOURNAL_MODE=WAL

# Uploads
UPLOAD_PATH=./uploads
MAX_FILE_SIZE=10485760
ALLOWED_FILE_TYPES=image/jpeg,image/png

# Rate Limiting
AUTH_RATE_LIMIT=10
AUTH_RATE_WINDOW=60000

# Socket.IO
SOCKET_CORS_ORIGIN=*
```

## Web Client Configuration

### Environment Variables

Create `.env` in `client/`:
```env
VITE_API_URL=http://localhost:3001/api
VITE_SOCKET_URL=http://localhost:3001
VITE_APP_NAME=Physcult
VITE_APP_VERSION=1.0.0
```

### Vite Configuration

`client/vite.config.js`:
```javascript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    host: true,
    proxy: {
      '/api': {
        target: 'http://localhost:3001',
        changeOrigin: true
      }
    }
  },
  build: {
    outDir: 'dist',
    sourcemap: false,
    minify: 'terser'
  }
});
```

## Mobile App Configuration

### Constants

`mobile/src/constants/config.js`:
```javascript
import Constants from 'expo-constants';

const extra = Constants.expoConfig?.extra || {};

export const API_URL = extra.apiUrl || 'http://localhost:3001';
export const SOCKET_URL = API_URL;
export const APP_NAME = 'Physcult';
export const APP_VERSION = '1.0.0';
export const ITEMS_PER_PAGE = 20;
export const MAX_PHOTOS_PER_ACTIVITY = 5;
```

---

# User Guide

End-user manual for Physcult.

## Getting Started

### Registration

1. Open Physcult app/website
2. Click **"Register"**
3. Fill in:
   - Name
   - Email
   - Password (min 6 characters)
   - Birthday (optional)
4. Click **"Create Account"**

### First Login

1. Enter email and password
2. Click **"Login"**
3. Enable Face ID/Touch ID (mobile)

## Recording Activities

### GPS-Tracked Workout

1. Go to **New Activity**
2. Select type (Run, Ride, Walk, etc.)
3. Click **"GPS Recording"**
4. Allow location permissions
5. Click **"Start"**
6. App tracks:
   - Distance
   - Duration
   - Route
   - Pace/Speed
   - Elevation

**During workout:**
- **Pause**: Stop temporarily
- **Resume**: Continue
- **Finish**: Complete workout

**After workout:**
1. Add title (auto-generated or custom)
2. Write description with #hashtags
3. Adjust metrics if needed
4. Add photos (up to 5)
5. Select gear
6. Click **"Save"**

### Manual Activity

1. Go to **New Activity**
2. Select type
3. Enter name
4. Fill in:
   - Duration (hours, minutes, seconds)
   - Distance (if applicable)
   - Calories
   - Elevation
5. Add description and photos
6. Click **"Save"**

## Social Features

### Following Users

1. Go to **Home** → **People**
2. Search for friends
3. Browse suggestions
4. Click **"Follow"**

### Engaging with Activities

- **React**: Choose emoji (❤️ 🔥 💪 👏)
- **Comment**: Share thoughts
- **Share**: Send to friends
- **Bookmark**: Save for later

### Stories

**Create:**
1. Click avatar with **"+"**
2. Choose photo or text
3. Add overlay text
4. Click **"Share"**

**View:**
1. Tap story ring
2. Tap right for next
3. Tap left for previous
4. React with emoji

## Messaging

1. Go to user's profile
2. Click message icon
3. Type message
4. Click send

**Features:**
- Text messages
- Photo sharing
- Read receipts
- Typing indicators
- Edit (before read)
- Delete messages

## Challenges & Goals

### Join Challenge

1. Go to **Challenges**
2. Browse available
3. Read details
4. Click **"Join"**
5. Progress updates automatically

### Create Challenge

1. Click **"+ Create"**
2. Fill in:
   - Title
   - Description
   - Activity type
   - Goal (distance/duration/count)
   - Period (start/end dates)
3. Click **"Create"**

### Set Goal

1. Go to **Goals**
2. Click **"+ Add"**
3. Configure:
   - Type (distance/duration/count)
   - Activity (specific or all)
   - Period (weekly/monthly)
   - Target value
4. Click **"Save"**

## Statistics

### View Stats

1. Go to **Stats** tab
2. See totals:
   - Workouts
   - Distance
   - Duration
   - Calories
3. Filter by period:
   - Week
   - Month
   - Year
   - All time

### Personal Records

1. Go to **Profile** → **Records**
2. View by category:
   - Longest distance
   - Longest duration
   - Fastest speed
   - Most elevation
   - Most calories

### Training Streak

- Current streak: Consecutive days
- Longest streak: Best run
- Calendar view
- Streak continues with 1+ activity/day

## Gear Management

### Add Gear

1. Go to **Gear**
2. Click **"+ Add"**
3. Enter:
   - Name (e.g., "Nike Pegasus 39")
   - Type (shoes, bike, skis, other)
   - Brand
4. Click **"Save"**

### Use Gear

When creating activities:
1. Select from dropdown
2. Usage tracked automatically:
   - Total distance
   - Activity count

**Tip:** Retire shoes at 500-800km!

## Settings

### Profile Settings

- Update personal info
- Change avatar
- Edit bio and location

### App Preferences

**Theme:**
- Light mode
- Dark mode
- System default

**Language:**
- English
- Russian
- Auto-detect

### Notifications

- Activity engagement
- New followers
- Challenge updates
- Messages
- Goal achievements

### Security (Mobile)

**Biometric:**
1. Go to **Settings** → **Security**
2. Enable **"Biometric Login"**
3. Confirm with Face ID/Touch ID

**PIN Code:**
1. Enable **"PIN Protection"**
2. Set 4-6 digit PIN

## Tips

### Recording Accurate Activities

- Allow location access
- Wait for GPS lock
- Keep phone charged
- Use pause at stops

### Growing Your Network

- Follow friends
- Like and comment
- Post regularly
- Use hashtags
- Complete profile

### Staying Motivated

- Set realistic goals
- Join challenges
- Maintain streak
- Engage with community
- Check progress

## Troubleshooting

### GPS Issues

- Enable location permissions
- Try outdoors with clear sky
- Restart app
- Check phone GPS settings

### Login Problems

- Check credentials
- Reset password
- Clear cache
- Reinstall if needed

### Photos Not Uploading

- Check file size (max 10MB)
- Use JPEG/PNG format
- Check storage space
- Compress images

---

# Support

For help:
- Check documentation in `docs/` folder
- Open GitHub issue
- Ask community

---

**End of Documentation**

---

© 2026 Physcult - Culture of Living in Harmony

# Planner with Firebase Integration

This is a Python planner application that integrates with Google Calendar, Google Tasks, and Firebase Firestore for enhanced data storage and synchronization.

## Features

- Google Calendar integration
- Google Tasks integration
- Firebase Firestore for task and event storage
- Task scheduling and management
- Event planning and optimization

## Setup Instructions

### 1. Install Dependencies

First, create a virtual environment and install the required packages:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Google API Setup

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Calendar API and Google Tasks API
4. Create credentials (OAuth 2.0 client ID) for a desktop application
5. Download the client secret files and rename them to:
   - `calendar_client_secret.json`
   - `task_client_secret.json`

### 3. Firebase Setup

1. Go to the [Firebase Console](https://console.firebase.google.com/)
2. Create a new Firebase project
3. Go to Project Settings > Service Accounts
4. Click "Generate new private key" to download the service account key
5. Rename the downloaded file to `firebase_service_account.json`
6. Enable Firestore Database in your Firebase project

### 4. Configuration

Make sure you have the following files in your project directory:

- `calendar_client_secret.json` (Google Calendar credentials)
- `task_client_secret.json` (Google Tasks credentials)
- `firebase_service_account.json` (Firebase service account key)

### 5. Run the Application

```bash
python planner_firebase.py
```

## Firebase Integration Features

The Firebase integration adds the following capabilities:

### Task Management

- **Backup Storage**: All tasks are automatically saved to Firebase Firestore
- **Cross-Device Sync**: Access your tasks from any device with Firebase access
- **Data Persistence**: Tasks remain available even if Google Tasks API is unavailable

### Event Management

- **Event Backup**: Calendar events are saved to Firebase for redundancy
- **Custom Metadata**: Store additional event information not available in Google Calendar

### Data Collections

The app creates two main Firestore collections:

#### `tasks` Collection

```json
{
  "name": "Task name",
  "due": "2025-09-15T10:00:00Z",
  "google_task_id": "google_task_id_here",
  "created_at": "timestamp",
  "completed": false,
  "completed_at": "timestamp_when_completed"
}
```

#### `events` Collection

```json
{
  "name": "Event name",
  "location": "Event location",
  "description": "Event description",
  "start": "2025-09-15T10:00:00Z",
  "end": "2025-09-15T11:00:00Z",
  "google_event_id": "google_event_id_here",
  "created_at": "timestamp"
}
```

## Usage

1. **List Pending Tasks**: View tasks from both Google Tasks and Firebase
2. **Add Tasks**: Tasks are automatically saved to both Google Tasks and Firebase
3. **Complete Tasks**: Mark tasks as complete in both systems
4. **Calendar Events**: Events are backed up to Firebase when created

## Troubleshooting

- **Firebase Connection Issues**: Ensure your `firebase_service_account.json` file is properly configured
- **Google API Issues**: Check that your client secret files are in the correct format
- **Permission Errors**: Make sure your service account has the necessary Firestore permissions

## Security Notes

- Keep your `firebase_service_account.json` file secure and never commit it to version control
- The same applies to your Google client secret files
- Consider using environment variables for sensitive configuration in production

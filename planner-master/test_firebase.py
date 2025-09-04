#!/usr/bin/env python3
"""
Firebase Test Script
This script tests the Firebase connection and basic operations.
"""

import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

def test_firebase():
    """Test Firebase connection and basic operations"""
    
    try:
        # Initialize Firebase
        if not firebase_admin._apps:
            cred = credentials.Certificate('firebase_service_account.json')
            firebase_admin.initialize_app(cred)
        
        db = firestore.client()
        print("✓ Firebase initialized successfully!")
        
        # Test writing data
        test_doc = {
            'test_field': 'test_value',
            'timestamp': firestore.SERVER_TIMESTAMP,
            'created_by': 'firebase_test_script'
        }
        
        doc_ref = db.collection('test').add(test_doc)
        print(f"✓ Test document created with ID: {doc_ref[1].id}")
        
        # Test reading data
        test_docs = db.collection('test').where('created_by', '==', 'firebase_test_script').stream()
        doc_count = 0
        for doc in test_docs:
            doc_count += 1
            print(f"✓ Read test document: {doc.id} => {doc.to_dict()}")
        
        print(f"✓ Found {doc_count} test document(s)")
        
        # Clean up test documents
        test_docs = db.collection('test').where('created_by', '==', 'firebase_test_script').stream()
        for doc in test_docs:
            doc.reference.delete()
            print(f"✓ Deleted test document: {doc.id}")
        
        print("✓ Firebase test completed successfully!")
        return True
        
    except FileNotFoundError:
        print("✗ Error: firebase_service_account.json file not found!")
        print("Please make sure you have downloaded your Firebase service account key")
        print("and saved it as 'firebase_service_account.json' in the project directory.")
        return False
        
    except Exception as e:
        print(f"✗ Firebase test failed: {e}")
        print("Please check your Firebase configuration and network connection.")
        return False

if __name__ == "__main__":
    print("Testing Firebase connection...")
    print("=" * 50)
    
    success = test_firebase()
    
    print("=" * 50)
    if success:
        print("Firebase is ready to use with your planner application!")
    else:
        print("Please fix the Firebase configuration before using the planner.")

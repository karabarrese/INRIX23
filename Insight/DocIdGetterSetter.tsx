import { collection, addDoc, updateDoc, doc, getDoc } from 'firebase/firestore';
import { db } from './components/config';

let docID, phoneNumber;

export function setDocID(id) {
    console.log("hi", id);
    docID = id;
    console.log("Set", docID);
}

export function getDocID() {
    console.log("Get", docID);
    return docID;
}

export async function getPhoneNumber(id) {
    try {
        const docRef = doc(db, 'user', id);
        const docSnap = await getDoc(docRef);

        if (docSnap.exists()) {
            // Access the data within the document
            const data = docSnap.data();
            const value = data.parentNumber;
            return value;
        } else {
            console.log('Document not found');
            return null; // or handle the case when the document doesn't exist
        }
    } catch (error) {
        console.error('Error getting document:', error);
        throw error; // handle the error as needed
    }
}
import { collection, addDoc, updateDoc, doc, getDoc } from 'firebase/firestore';
import { db } from './components/config';

export const add_contacts = async (parentName: any, parentNumber: any, id: any) => {
  try {
    console.log("Entered function");
    console.log(parentName, parentNumber);

    const usersCollectionRef = collection(db, 'users');

    // Construct the document reference using the document ID
    const userDocRef = doc(usersCollectionRef, id);

    // Check if the document exists
    const userDocSnapshot = await getDoc(userDocRef);
    if (userDocSnapshot.exists()) {
      // Update the document with new data
      await updateDoc(userDocRef, {
        parentName: parentName,
        parentNumber: parentNumber,
      });

      console.log("Data submitted to the database");
    } else {
      console.log("Document with ID does not exist:", id);
    }
  } catch (error) {
    console.error(error);
  }
  console.log("Finished Function");
};

export const add_user_details = async (username: any, password: any) => {
  try {
    console.log("Entered function");
    console.log(username, password);

    const usersCollectionRef = collection(db, 'users');

    // Add document to the collection
    const docRef = await addDoc(usersCollectionRef, {
      username: username,
      password: password,
      parentName: "",
      parentNumber: "",
    });

    // Get the key of the newly added document
    const docKey = docRef.id;

    console.log("Data submitted to the database");
    console.log("Document key:", docKey);

    return docKey; // Return the document key
  } catch (error) {
    console.error(error);
    throw error; // Re-throw the error to handle it in the calling code if needed
  }
};

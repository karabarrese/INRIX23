import { collection, addDoc } from 'firebase/firestore';
import { db } from './components/config';

export const add_contacts = async (parentName: any, parentNumber: any, id: any) => {
  try {
    console.log("Entered function");
    console.log(parentName, parentNumber)

    const usersCollectionRef = collection(db, id);

    await addDoc(usersCollectionRef, {
      parentName: parentName,
      parentNumber: parentNumber,
      email: "None",
      username: "None"
    });

    console.log("Data submitted to the database");
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
      parentName: "None",
      parentNumber: "None"
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

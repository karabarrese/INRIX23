// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyC32_ivKwcbcNbQf4wK2WlgtTXYn8VHrsI",
    authDomain: "inrix23.firebaseapp.com",
    projectId: "inrix23",
    storageBucket: "inrix23.appspot.com",
    messagingSenderId: "461213086622",
    appId: "1:461213086622:web:37f5668b0274651207dc8f",
    measurementId: "G-95G6Q60V5F"
  };

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

const analytics = getAnalytics(app);


export { db };
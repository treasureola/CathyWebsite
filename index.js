// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAZajC4Mjx1gJuRqH0fmfWXjUvYFe_AYJY",
  authDomain: "cathy-b354a.firebaseapp.com",
  databaseURL: "https://cathy-b354a-default-rtdb.firebaseio.com",
  projectId: "cathy-b354a",
  storageBucket: "cathy-b354a.firebasestorage.app",
  messagingSenderId: "804564901869",
  appId: "1:804564901869:web:2d9e66ed9d175efae051e4",
  measurementId: "G-Q1ZGEPM91T"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
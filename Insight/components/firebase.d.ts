declare module 'components/config' {
    import { Firestore } from 'firebase/firestore';
    const firebaseConfig: {
      apiKey: string;
      authDomain: string;
      projectId: string;
      storageBucket: string;
      messagingSenderId: string;
      appId: string;
      measurementId?: string;
    };
    export const db: Firestore;
    export { firebaseConfig };
  }
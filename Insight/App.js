import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, SafeAreaView, Button } from 'react-native';
import WelcomeScreen from './app/screens/WelcomeScreen';
import LocationPage from './app/screens/LocationPage';
import DrivingFactPage from './app/screens/DrivingFactPage';
import ContactsScreen from './app/screens/ContactsPage';
// import { NavigationContainer } from '@react-navigration/native';
// import { createNativeStackNavigator} from '@react-navigration/native-stack';
 
//App Component
export default function App() { 
  const handlePress = () => console.log("Text pressed")
  
  /*return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="WelcomeScreen">
        <Stack.Screen name="WelcomeScreen" component={WelcomeScreen} />
        <Stack.Screen name="LoginScLoreen" component={LoginScreen} />
        <Stack.Screen name="FactHome" component={FactHomeScreen} />
        <Stack.Screen name="Contacts" component={ContactsScreen} />
        <Stack.Screen name="LocationPg" component={LocationPgScreen} />
        <Stack.Screen name="Driving" component={DrivingScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
  */
};

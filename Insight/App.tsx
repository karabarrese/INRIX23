import SignupScreen from './SignupScreen';
import docId from './SignupScreen';
import ContactsScreen from './ContactsScreen';
import HomeScreen from './HomeScreen';
import DrivingFact from './DrivingFact';
import React, { Component } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';

const Stack = createNativeStackNavigator();

// const AppNavigator = () => (
//   <NavigationContainer>
//     <Stack.Navigator>
//       <Stack.Screen name="Signup" component={SignupScreen} />
//       <Stack.Screen name="Contacts" component={ContactsScreen} />
//     </Stack.Navigator>
//   </NavigationContainer>
// );


class App extends Component {
  render() {
    return (
      <NavigationContainer>
        <Stack.Navigator initialRouteName='HomeScreen'>
          <Stack.Screen
            name="SignUp"
            component={SignupScreen} 
          />
          <Stack.Screen
            name="ContactsScreen"
            component={ContactsScreen} 
          />
          <Stack.Screen
            name="HomeScreen"
            component={HomeScreen} 
          />
          <Stack.Screen
            name="DrivingFact"
            component={DrivingFact} 
          />
        </Stack.Navigator>
      </NavigationContainer>
    );
  }
}

export default App;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

import SignupScreen from './SignupScreen';
import docId from './SignupScreen';
import ContactsScreen from './ContactsScreen';

import React, { Component } from 'react';
import { View, Text } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

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
        <Stack.Navigator initialRouteName='SignUp'>
          <Stack.Screen
            name="SignUp"
            component={SignupScreen} 
          />
          <Stack.Screen
            name="Contacts"
            component={ContactsScreen} 
          />
        </Stack.Navigator>
      </NavigationContainer>
    );
  }
}

export default App;


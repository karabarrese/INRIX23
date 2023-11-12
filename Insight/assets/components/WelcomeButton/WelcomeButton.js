import React from 'react';
import {View, Text, StyleSheet, Pressable} from 'react-native';

const WelcomeButton = ({ onPress }) => {
    return (
        <Pressable onPress={onPress} style={styles.container}>
            <Text style={styles.text}>Start now!</Text>
        </Pressable>
    );
}; 

const styles = StyleSheet.create({
   container: {
    backgroundColor: "#E0EEC6", 
    width: 217,
    height: 60,
    padding: 15,
    marginVertical: 5, 

    alignItems: 'center', 
    justifyContent: 'center',
    borderRadius: 5, 
    bottom: 0,
    borderRadius: 30,
   },

   text: {
    fontWeight: 'bold',
    color: '#243E36',
    fontSize: 23
   }


})
export default WelcomeButton;
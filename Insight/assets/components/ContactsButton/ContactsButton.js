import React from 'react';
import {View, Text, StyleSheet, Pressable} from 'react-native';

const ContactsButton = ({ onPress}) => {
    return (
        <Pressable onPress={onPress} style={styles.container}>
            <Text style={styles.text}>contacts</Text>
        </Pressable>
    );
}; 

const styles = StyleSheet.create({
   container: {
    backgroundColor: "#962626", 
    width: 140,
    height: 175,
    padding: 15,
    marginVertical: 5, 

    alignItems: 'center', 
    borderRadius: 5, 
    bottom: '61%',
    left: '20%',
    borderRadius: 30
   },

   text: {
    fontWeight: 'bold',
    color: '#FFD6D6',
    fontSize: 28,
    top: '72%'
   }


})
export default ContactsButton;
import React from 'react';
import {View, Text, StyleSheet, Pressable} from 'react-native';

const BackButton = ({ onPress }) => {
    return (
        <Pressable onPress={onPress} style={styles.container}>
            <Text style={styles.text}>Back</Text>
        </Pressable>
    );
}; 

const styles = StyleSheet.create({
   container: {
    backgroundColor: "#962626", 
    width: 118,
    height: 66,
    padding: 15,
    marginVertical: 5, 

    alignItems: 'center', 
    justifyContent: 'center',
    borderRadius: 5, 
    top: '20%',
    left: '40%',
    borderRadius: 30
   },

   text: {
    fontWeight: 'bold',
    color: '#E0EEC6',
    fontSize: 23
   }


})
export default BackButton;
// DrivingFact.js
import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Image, Pressable } from 'react-native';
import { add_user_details } from './addDataToDatabase'; // Adjust the path accordingly

class DrivingFact extends React.Component {
    constructor(props) {
        super(props);
    
        this.state = {

        };
      }

    handleSubmit = async () => {

        console.log("Want to go to drive page");
        //this.props.navigation.navigate("SignUp");
        // this.props.navigation.navigate("Contacts");
        return;
    };
    wandleSubmit = async () => {

        console.log("Want to go to contacts page");
        this.props.navigation.navigate("ContactsScreen");
        // this.props.navigation.navigate("Contacts");
        return;
    };

    render() {
        return (
            <View style={styles.background}>
            <View style={styles.line}>
            </View>
            <Text style={styles.text}>
                Distracted 
                {'\n'}
                Driving
            </Text>
            <Pressable onPress={this.handleSubmit} style={styles.container}>
            <Text style={styles.text}>drive</Text>
            </Pressable>
            <Pressable onPress={this.wandleSubmit} style={styles.container}>
            <Text style={styles.text}>contacts</Text>
            </Pressable>
            <Image 
                style={styles.contacts}
                source={require('./assets/Contacts.png')}
            />
            <Image 
                style={styles.destination}
                source={require('./assets/Destination.png')}
            />
            <View style={styles.fact}>
                <Text style={styles.text1}>
                    Did you know ____ 
                    {'\n'}
                    accidents happened   
                    {'\n'}
                    in your area due to  
                    {'\n'}
                    distracted driving 
                    {'\n'}
                    in your 
                    {'\n'}
                    neighborhood?
                </Text>
            </View>
            </View>
        );
    }
}


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

  export default DrivingFact;
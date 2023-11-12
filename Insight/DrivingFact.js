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

    driveSubmit = async () => {
        console.log("Want to go to drive page");
        //this.props.navigation.navigate("SignUp");
        this.props.navigation.navigate("LocationScreen");
        return;
    };
    contactsSubmit = async () => {
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
            <Pressable onPress={this.driveSubmit} style={styles.container1}>
            <Text style={styles.text2}>drive</Text>
            </Pressable>
            <Pressable onPress={this.contactsSubmit} style={styles.container2}>
            <Text style={styles.text3}>contacts</Text>
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
                <Text style={styles.textM}>
                Did you know:
                {'\n'}
                Car crashes are the leading cause 
                {'\n'}
                of death in the United States for 
                {'\n'}
                people ages 1 to 54
            </Text>
            </View>
            
            </View>
        );
    }
}


const styles = StyleSheet.create({

    background: {
        backgroundColor: "#E0EEC6",
        flex: 1
      },
      
      line:{
        backgroundColor: '#7CA982',
        width: 5,
        height: 484,
        left: '10%',
        top: '15%',
      },

   text: {
    fontWeight: 'bold',
    color: '#243E36',
    fontSize: 55, 
    left: '15%',
    bottom: '70%',
    letterSpacing: 5,
    lineHeight: 75,
    paddingVertical: 10,
    //fontFamily: "PalanquinDark Bold",
  },
  textM:{
    fontWeight: 'bold',
    color: '#243E36',
    fontSize: 15, 
    left: '2%',
    bottom: '130%',
    letterSpacing: 1,
    paddingVertical: 10,
    //fontFamily: "PalanquinDark Bold",
  },

  contacts: {
    left: '20%',
    width: 96, 
    height: 96, 
    bottom: '123%'

  },

  destination: {
    width: 60,
    height: 100, 
    position: 'absolute',
    right: '16%',
    bottom: '43%'
  },

  fact: {
    width: 335, 
    height: 207,
    backgroundColor: '#243E36',
    bottom: '68%',
    left: '15%'
  }, 

  text1: {
    color: '#243E36',
    fontSize: 18,
    letterSpacing: 7,
    lineHeight: 20,
    paddingVertical: 10,
    fontWeight: 'bold',
    left: '5%',
    top: '10%'
  },

   container1: {
    backgroundColor: "#962626", 
    width: 140,
    height: 160,
    padding: 15,
    marginVertical: 5, 

    alignItems: 'center', 
    borderRadius: 5, 
    bottom: '70%',
    left: '58%',
    borderRadius: 30
   },

   text2: {
    fontWeight: 'bold',
    color: '#FFD6D6',
    fontSize: 28,
    top: '73%'
   }, 

   container2: {
    backgroundColor: "#962626", 
    width: 140,
    height: 160,
    padding: 15,
    marginVertical: 5, 

    alignItems: 'center', 
    borderRadius: 5, 
    bottom: '98%',
    left: '15%',
    borderRadius: 30
   },

   text3: {
    fontWeight: 'bold',
    color: '#FFD6D6',
    fontSize: 25,
    top: '73%'
   }

})

  export default DrivingFact;
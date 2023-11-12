// HomeScreen.js
import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Image, Pressable } from 'react-native';
import { add_user_details } from './addDataToDatabase'; // Adjust the path accordingly

class HomeScreen extends React.Component {
    constructor(props) {
        super(props);
    
        this.state = {

        };
      }

    handleSubmit = async () => {

        console.log("Function returned a");
        this.props.navigation.navigate("SignUp");
        // this.props.navigation.navigate("Contacts");
    };

    render() {
        return (
            <View style={styles.background}>
            <View style={styles.lightgreenbackground}> 
                <Text style={styles.text}>insight</Text>
            </View>
            <Image
                style={styles.image1}
                source={require('./assets/GPS.png')}
            />
            <View>
                <View style={styles.line1}></View>
                <Text style={styles.blurb}>[powered by INRIX]</Text>
            </View>
            <Image 
                style={styles.image}
                source={require('./assets/Cars.png')}
            />
            <Pressable onPress={this.handleSubmit} style={styles.container}>
            <Text style={styles.text}>Start now!</Text>
            </Pressable>

            <View>
                <View style={styles.line2}></View>
                <View style={styles.line3}></View>
            </View>
              <TouchableOpacity onPress={this.handleSubmit} style={styles.button}>
                  <Text style={{ color: 'white', fontWeight: 'bold', fontSize: 25}}>Next</Text>
              </TouchableOpacity>
        
        
              <StatusBar style="auto" />
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

  export default HomeScreen;
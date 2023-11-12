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
                    <Text style={styles.text1}>Start now!</Text>
                </Pressable>
                
                <View>
                    <View style={styles.line2}></View>
                    <View style={styles.line3}></View>
                </View>
            </View>
          );
    }
}


const styles = StyleSheet.create({
    container: {
        backgroundColor: "#962626",
        width: 217, 
        height: 60, 
        padding: 15, 
        marginVertical: 5, 
        bottom: '200%' ,

        alignItems: 'center',
        justifyContent: 'center', 
        borderRadius: 30, 
        bottom: 0, 
        left: '30%'
    },

    text1: {
        fontWeight: 'bold', 
        color: '#E0EEC6',
        fontSize: 23
    },

    background: {
        backgroundColor: "#243E36",
        flex: 1
    },

    lightgreenbackground: {
        backgroundColor:"#E0EEC6",
        position: "1px",
        width: 226,
        height: 115,
        top: '18%', 
        left: 30, 
        justifyContent: "center", 
        alignItems: "center",
        borderRadius: 5, 
    },
    
    text: {
        fontWeight: 'bold',
        color: '#243E36',
        fontSize: 50, 
    },
    
    image: {
        // Adjust position using the following properties:
// or 'relative' depending on your layout needs
        left: 30, // Adjust top position
        top: '5%',
        width: 285,
        height: 204,

    }, 

    line1: {
        backgroundColor: "#7CA982",
        width: 205,
        height: 3,
        bottom: '30%',
        left: 30
    },

    blurb: {
        fontStyle: 'italic',
        color: '#E0EEC6',
        fontSize: 20, 
        left: '8%',
        bottom: '1%',
    }, 

    image1: {
        width: 65, 
        height: 125,
        left: '75%',
        bottom: '3%', 
        padding: '1%' 
    },

    line2: {
        backgroundColor: "#7CA982",
        width: 159,
        height: 3,
        top: '80%',
        left: '45%'
    },

    line3: {
        backgroundColor: "#7CA982",
        width: 118,
        height: 3,
        top: '200%',
        left: '55%'
    }
});

  export default HomeScreen;
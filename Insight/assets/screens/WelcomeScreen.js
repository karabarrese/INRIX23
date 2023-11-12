import React from "react";
import { ImageBackground } from "react-native-web";
import { StyleSheet, Text, View, Image, SafeAreaView, Button } from 'react-native';

export default function WelcomeScreen() {
    const onPressed = () => {
        console.warn('onPressed')
    }
    return (
        <View style={styles.background}>
            <View style={styles.lightgreenbackground}> 
                <Text style={styles.text}>insight</Text>
            </View>
            <Image
                style={styles.image1}
                source={require('../assets/GPS.png')}
            />
            <View>
                <View style={styles.line1}></View>
                <Text style={styles.blurb}>[powered by INRIX]</Text>
            </View>
            <Image 
                style={styles.image}
                source={require('../assets/Cars.png')}
            />
            <WelcomeButton onPress={onPressed}/>

            <View>
                <View style={styles.line2}></View>
                <View style={styles.line3}></View>
            </View>
        </View>


    )
}

const styles = StyleSheet.create({
    background: {
        backgroundColor: "#243E36",
        flex: 1
    },

    lightgreenbackground: {
        backgroundColor:"#E0EEC6",
        position: "1px",
        width: 226,
        height: 115,
        top: 200, 
        left: 60, 
        justifyContent: "center", 
        alignItems: "center",
        borderRadius: 5, 
    },
    
    text: {
        fontWeight: 'bold',
        color: '#243E36',
        fontSize: 50, 
        fontFamily: "PalanquinDark Bold",
    },
    
    image: {
        // Adjust position using the following properties:
// or 'relative' depending on your layout needs
        left: 60, // Adjust top position
        top: '20%',
        width: 285,
        height: 204
    }, 

    line1: {
        backgroundColor: "#7CA982",
        width: 205,
        height: 3,
        top: 85,
        left: '16%'
    },

    blurb: {
        fontStyle: 'italic',
        color: '#E0EEC6',
        fontSize: 20, 
        left: '18%',
        top: '300%',
    }, 

    image1: {
        width: 65, 
        height: 125,
        left: '75%',
        top: '9%', 
        padding: '1%' 
    },

    line2: {
        backgroundColor: "#7CA982",
        width: 159,
        height: 3,
        top: 150,
        left: '48%'
    },

    line3: {
        backgroundColor: "#7CA982",
        width: 118,
        height: 3,
        top: 160,
        left: '58%'
    }
});
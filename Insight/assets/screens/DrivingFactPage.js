import React from 'react'
import { StyleSheet, Text, View, Image, SafeAreaView, Button } from 'react-native';
import ContactsButton from '../components/ContactsButton/ContactsButton';
import DriveButton from '../components/DriveButton/DriveButton';

export default function DrivingFactPage() {

  const onPressed = () => {
    console.warn('onPressed')
  }
  
  return (
    <View style={styles.background}>
      <View style={styles.line}>
      </View>
      <Text style={styles.text}>
        Distracted 
        {'\n'}
        Driving
      </Text>
      <DriveButton onPress={onPressed}/>
      <ContactsButton onPress={onPressed}/>
      <Image 
        style={styles.contacts}
        source={require('../assets/Contacts.png')}
      />
      <Image 
        style={styles.destination}
        source={require('../assets/Destination.png')}
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
  )
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
    bottom: '42%',
    letterSpacing: 5,
    lineHeight: 75,
    paddingVertical: 10,
    //fontFamily: "PalanquinDark Bold",
  },
  
  Greenimage: {
      // Adjust position using the following properties:
// or 'relative' depending on your layout needs
      left: '65%', // Adjust top position
      width: 279,
      height: 550,
      bottom: '50%',
      position: 'absolute'
  },

  contacts: {
    left: '25%',
    width: 96, 
    height: 96, 
    bottom: '80%'

  },

  destination: {
    width: 60,
    height: 100, 
    position: 'absolute',
    right: '16%',
    bottom: '53%'
  },

  fact: {
    width: 335, 
    height: 207,
    backgroundColor: '#243E36',
    bottom: '68%',
    left: '15%'
  }, 

  text1: {
    color: '#E0EEC6',
    fontSize: 18,
    letterSpacing: 7,
    lineHeight: 20,
    paddingVertical: 10,
    fontWeight: 'bold',
    left: '5%',
    top: '10%'
  }
});
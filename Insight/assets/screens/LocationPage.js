import React from 'react'
import { StyleSheet, Text, View, Image, SafeAreaView, Button } from 'react-native';
import EnterLocationButton from '../components/EnterLocationButton/EnterLocationButton';
import BackButton from '../components/BackButton/BackButton';

export default function LocationPage() {

  const onPressed = () => {
    console.warn('onPressed')
  }
  return (
    <View style={styles.background}>
      <View>
        <View style={styles.darkgreenoutline}> 
        <Text style={styles.text}>WHERE
        {'\n'}
        ARE 
        {'\n'}
        YOU 
        {'\n'}
        GOING?
        </Text>
        </View>
      </View>
      <EnterLocationButton onPress={onPressed}/>
      <BackButton onPress={onPressed}/>
      <Image 
          style={styles.Greenimage}
          source={require('../assets/GreenCar(1).png')}
      />
  </View>
  )
}

const styles = StyleSheet.create({
  background: {
    backgroundColor: "#E0EEC6",
    flex: 1
  },
  
  darkgreenoutline:{
    backgroundColor: '#E0EEC6',
    width: 350,
    height: 550,
    right: '30%',
    top: '19%',
    borderWidth: 7, // Set the width of the border
    borderColor: '#243E36', // Set the color of the border
  },

  text: {
    fontWeight: 'bold',
    color: '#243E36',
    fontSize: 55, 
    left: '38%',
    letterSpacing: 1,
    lineHeight: 100,
    paddingVertical: 10,
    fontFamily: "PalanquinDark Bold",
  },
  
  Greenimage: {
      // Adjust position using the following properties:
// or 'relative' depending on your layout needs
      left: '65%', // Adjust top position
      width: 279,
      height: 550,
      bottom: '60%',
  }
});
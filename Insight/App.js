import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Platform } from 'react-native';
import React, { useState, useEffect } from 'react';
import * as Location from 'expo-location';


export default function App() {
  const [location, setLocation] = useState(null);
  const [errorMsg, setErrorMsg] = useState(null);

  useEffect(() => {
    (async () => {
      
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') {
        setErrorMsg('Permission to access location was denied');
        return;
      }

      let location = await Location.getCurrentPositionAsync({});
      setLocation(location);
    })();
  }, []);

  let text = 'Waiting..';
  if (errorMsg) {
    text = errorMsg;
  } else if (location) {
    text = JSON.stringify(location);
  }

  return (
    <View style={styles.container}>
      <Text style={styles.paragraph}>{text}</Text>
    </View>
  );


 /*
  url = "https://maps.googleapis.com/maps/api/directions/json";
  
  const coordinates = {
    longitude: 37,
    latitude: -121
  };
  /*const location = {
    latLng: coordinates
  };*/

  /*
  const waypoint =
  {
    //"via": boolean,
    //"vehicleStopover": boolean,
    //"sideOfRoad": boolean,
  
    // Union field location_type can be only one of the following:
    "location": {
      coordinates
    },
    //"placeId": string,
    //"address": string
    // End of list of possible types for union field location_type.
  }
  const route_string = {

  }
*/
}
/*
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});*/

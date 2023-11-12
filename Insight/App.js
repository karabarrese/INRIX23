import { StatusBar } from 'expo-status-bar';
<<<<<<< Updated upstream
import { StyleSheet, Text, View } from 'react-native';
//import {GetLocation} from 'react-native-get-location'

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Open up App.js to start working on your app!</Text>
      <StatusBar style="auto" />
    </View>
  );
}
=======
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
 
  url = "https://maps.googleapis.com/maps/api/directions/json";
  
  class LatLng {
    constructor(lat, lon) {
      this.lat = lat;
      this.lon = lon;
    }
  }

  /*function makeLatLng(lat,lon)
  {
    return {
      "latitude": lat,
      "longitude": lon
    };
  }*/
  //using this to make a LatLng
  //const location1 = new LatLng(37,-121);
  waypoint =
  {
    "via": boolean,
    "vehicleStopover": boolean,
    "sideOfRoad": boolean,
  
    // Union field location_type can be only one of the following:
    "location": {
      object (Location)
    },
    "placeId": string,
    "address": string
    // End of list of possible types for union field location_type.
  }
  params = 
  {}

  return (
    <View style={styles.container}>
      <Text style={styles.paragraph}>{text}</Text>
    </View>
  );
} 
>>>>>>> Stashed changes

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
<<<<<<< Updated upstream
});

/*GetLocation.getCurrentPosition({
  enableHighAccuracy: true,
  timeout: 60000,
})
.then(location => {
  console.log(location);
})
.catch(error => {
  const { code, message } = error;
  console.warn(code, message);
})*/
=======
});
>>>>>>> Stashed changes

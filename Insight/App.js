import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, AppState, Platform } from 'react-native';
import React, { useState, useEffect, useRef } from 'react'
import { Accelerometer } from 'expo-sensors';
import * as Location from 'expo-location';

export default function App() {
  // Get incident data from flask backend
  const [data, setData] = useState([{}])

  useEffect(() => {
    console.log("useEffect")
    fetch("http://172.31.181.212:5001/incidents").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        // console.log(data)
        // console.log(data.incidents)
      }
    )
  }, [])

  // Detect app state to see if user leaves the app
  const appState = useRef(AppState.currentState)
  const [appStateVisible, setAppStateVisible] = useState(appState.current) 
  
  useEffect(() =>{
    AppState.addEventListener("change", _handleAppStateChange)
    return () => {
      AppState.removeEventListener("change", _handleAppStateChange)
    }
  }, [])
  
  const _handleAppStateChange = (nextAppState) => {
    if(appState.current.match(/active/) && nextAppState === "inactive" ){
      console.log("User clicked off app")
      // try {
      //   fetch("http://172.31.181.212:5001/sendMessage", {
      //     method: 'POST',
      //     headers: {
      //       'Content-Type': 'application/json',
      //     }
      //   });

      // }
      // catch(error){
      //   console.error('Error: ', error)
      // }
    }
    appState.current = nextAppState
    setAppStateVisible(appState.current)
    // console.log("AppState: ", appState.current)
  }

  // Get segment speed and see if user is driving too fast
  useEffect(() => {
    fetch("http://172.31.181.212:5001/segmentSpeed").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        // console.log(data.currentSegmentSpeed)
      }
    )
  }, [])
  prevAcceleration=0
  curAcceleration=0
  const [{ x, y, z }, setData2] = useState({
    x: 0,
    y: 0,
    z: 0,
  });
  const [subscription, setSubscription] = useState(null);

  Accelerometer.setUpdateInterval(1000);

  const _subscribe = () => {
    setSubscription(Accelerometer.addListener(setData2));
  };

  const _unsubscribe = () => {
    subscription && subscription.remove();
    setSubscription(null);
  };
  
  useEffect(() => {
    _subscribe();
    return () => _unsubscribe();
  }, []);
  console.log("y", Math.abs(y))
  console.log("currentSegmentSpeed", (data.currentSegmentSpeed || 15))
  if(y * 8 > (data.currentSegmentSpeed || 15)){
    console.log("moving too fast")
    // try {
    //   fetch("http://172.31.181.212:5001/sendSpeedMessage", {
    //     method: 'POST',
    //     headers: {
    //       'Content-Type': 'application/json',
    //     }
    //   });

    // }
    // catch(error){
    //   console.error('Error: ', error)
    // }
  }
    // prevAcceleration = curAcceleration;
    // curAcceleration = z;
    // velocity = (curAcceleration + prevAcceleration)/2*1 //meters per second
    // milesPerMeter = 0.000621371
    // secondsPerHour = 3600
    // velocityMPH = velocity * milesPerMeter * secondsPerHour * 20
    // console.log(velocityMPH)
    // mph
    // if(velocity>0.75){
    //   console.log("moving too fast in z")
    // }  
  // }, []);

  // Return/display incident data
  return (
    <View style={styles.container}>
      <Text>Test</Text>
      {(typeof data.incidents === 'undefined') ? (
        <Text>Loading...</Text>
      ) : (
        <View>
          <Text>{data.incidents[0][0][0]}</Text>
          <Text>{data.incidents[0][0][1]}</Text>
          <Text>{data.incidents[0][1]}</Text>
        </View>
        // data.message.map((data, i) => (
        //   <View>
        //     <Text>{data.incidents[i][0][0]}</Text>
        //     <Text>{data.incidents[i][0][1]}</Text>
        //   </View>
        // ))
      )}
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

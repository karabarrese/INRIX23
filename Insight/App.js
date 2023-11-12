import React from 'react';
import MapView, { Callout, Marker } from 'react-native-maps';
import { StyleSheet, SafeAreaView, Text, View } from 'react-native';
import { useState, useEffect, useRef } from 'react';
import { StatusBar } from 'expo-status-bar';
import { Accelerometer } from 'expo-sensors';

export default function App() {

    const [data, setData] = useState([{}])
  
    useEffect(() => {
      console.log("useEffect")
      fetch("http://172.31.181.212:5001/incidents").then(
        res => res.json()
      ).then(
        data => {
          setData(data)
          //console.log(data)
          // console.log(data.incidents)
        }
      )
  
      // console.log(res)
    }, [])

   const incidents = [
      {
          latitude: 37.74089,
          //data.incidents[0][0][1],
          longitude: -122.39313,
          //data.incidents[0][0][0],
          description: 'Quint St: no through traffic \n allowed from Newcomb Ave \n to Jerrold Ave'
      },
      {
          latitude: 38.55308,
          //data.incidents[1][0][1],
          longitude: -122.45669,
          //data.incidents[1][0][0]
          description: 'Howell Mountain Rd: road closed from \n Conn Valley Rd to Deer Park Rd'
      },
      {
          latitude: 37.48662889005637,
          //data.incidents[2][0][1],
          longitude: -122.22631989787935,
          //data.incidents[2][0][0]
          description: 'Broadway: road permanently closed \n from Broadway St to Main St'
      },
      {
          latitude: 37.48652003669021,
          //data.incidents[3][0][1],
          longitude: -122.22914906458071,
          //data.incidents[3][0][0]
          description: 'Theatre Way N/B: road permanently closed \n between Winslow St and Broadway'
      },
      {
          latitude: 37.71233,
          //data.incidents[4][0][1],
          longitude: -122.41826,
          //data.incidents[4][0][0]
          description: 'Sunnydale Ave: no through traffic allowed \n from Hahn St to Santos St'
      },
    ]

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
  // console.log("y", Math.abs(y))
  // console.log("currentSegmentSpeed", (data.currentSegmentSpeed || 15))
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
    <SafeAreaView style={styles.container}>
      <MapView 
      style={styles.map}
      initialRegion={{
        latitude: 37.78825,
        longitude: -122.4324,
        latitudeDelta: 0.0922,
        longitudeDelta: 0.0421,
      }}
      >
      {incidents.map((item,description) => {
        return(
          <Marker coordinate={item}>
            <Callout>
              <Text>{item.description}</Text>
            </Callout>
          </Marker>
          
        )
      })
      }
      
      </MapView>

      {(typeof data.incidents === 'undefined') ? (
        <Text>Loading...</Text>
      ) : (
        <SafeAreaView>
          <Text style={styles.title}>
          Lock Down Mode!!!
          </Text>
          <Text style={styles.inc}>
          Eyes off the screen until you reach your destination
          </Text>
        </SafeAreaView>
        // data.message.map((message, i) => (
        //   <Text key={i}>{message}</Text>
        // ))
      )}
      <StatusBar style="auto" />
    </SafeAreaView>
  );
}


const styles = StyleSheet.create({
  container: {
    marginTop: 80,
    flex: 1,
    marginLeft: 20,
    marginRight: 20,
  },
  map: {
    alignContent: 'center',
    justifyContent: 'center',
    width: '100%',
    height: '70%',
  },
  title:{
    fontWeight: 'bold',
    paddingTop: 50,
    fontSize: 18,
    paddingBottom: 10,

  },
  inc: {
    
    fontSize: 18,
    alignContent: 'center',
    justifyContent: 'center',
  
  },
});

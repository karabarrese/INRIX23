import React from 'react';
import MapView, { Callout, Marker } from 'react-native-maps';
import { StyleSheet, SafeAreaView, Text } from 'react-native';
import { useState, useEffect } from 'react';
import { StatusBar } from 'expo-status-bar';

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

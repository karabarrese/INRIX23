import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, AppState } from 'react-native';
import React, { useState, useEffect, useRef } from 'react'

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
      AppState.removeEventListern("change", _handleAppStateChange)
    }
  }, [])
  
  const _handleAppStateChange = (nextAppState) => {
    if(appState.current.match(/active/) && nextAppState === "inactive" ){
      console.log("User clicked off app")
    }
    appState.current = nextAppState
    setAppStateVisible(appState.current)
    // console.log("AppState: ", appState.current)
  }

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
        // data.message.map((message, i) => (
        //   <Text key={i}>{message}</Text>
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

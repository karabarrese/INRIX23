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

    // communicate with flask backend
    // useEffect(() =>{
    //   return fetch(`http://172.31.181.212:5001/add`,{
    //     'method':'POST',
    //     headers : {
    //       'Content-Type':'application/json'
    //     },
    //   })
    //   .then(response => response.json())
    //   .catch(error => console.log(error))
    // }, [])
    // onClick= () => {
    //   const todo = { content }
    //   const response = fetch("http://172.31.181.212:5001/add_todo", {
    //   method: "POST",
    //   headers: {
    //   'Content-Type' : 'application/json'
    //   },
    //   body: JSON.stringify(todo)
    //   })
    // }
    // function handlePostQuery(){
    //   console.log("handle called")
    //   var myParams = {
    //     data: "query"
    //   }
    //   axios.post('http://172.31.181.212:5001/add_todo', myParams)
    //     .then(function(response){
    //       console.log(response);
    //   //Perform action based on response
    //   })
    //   .catch(function(error){
    //       console.log(error);
    //   //Perform action based on error
    //   });
    // }


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

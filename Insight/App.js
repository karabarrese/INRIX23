import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import React, { useState, useEffect } from 'react'

export default function App() {
  const [data, setData] = useState([{}])

  useEffect(() => {
    console.log("useEffect")
    fetch("http://172.31.181.212:5001/").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
        console.log(data.message)
      }
    )

    // console.log(res)
  }, [])

  return (
    <View style={styles.container}>
      <Text>Test</Text>
      {(typeof data.message === 'undefined') ? (
        <Text>Loading...</Text>
      ) : (
        <Text>{data.message}</Text>
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

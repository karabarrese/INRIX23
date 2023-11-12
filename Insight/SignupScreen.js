// SignupScreen.tsx
import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { View, Text, TextInput, TouchableOpacity, StyleSheet,Image } from 'react-native';
import { add_user_details } from './addDataToDatabase'; // Adjust the path accordingly
import { setDocID } from './DocIdGetterSetter'

let username="", password="";


class SignupScreen extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      password: "",
    };
  }

  handleSubmit = async () => {
    console.log('Submitted:', this.state.username, this.state.password);

    let docId;
    docId = await add_user_details(this.state.username, this.state.password);
    console.log ("docId", docId)
    setDocID(docId);
    // getDocID();

    console.log("Function returned a");
    this.props.navigation.navigate("DrivingFact");
    // this.props.navigation.navigate("Contacts");
  };

  render() {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <Text>Signup Screen</Text>

        <TextInput
          value={this.state.username}
          onChangeText={(text) => this.setState({ username: text })}
          placeholder="Username"
          style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 10, paddingHorizontal: 10, width: 200 }}
        />

        <TextInput
          value={this.state.password}
          onChangeText={(text) => this.setState({ password: text })}
          placeholder="Password"
          style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 10, paddingHorizontal: 10, width: 200 }}
        />

        <TouchableOpacity
          onPress={this.handleSubmit}
          style={{ backgroundColor: 'blue', padding: 10, borderRadius: 5, marginTop: 10 }}
        >
          <Text style={{ color: 'white' }}>Submit</Text>
        </TouchableOpacity>

        <StatusBar backgroundColor="" />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },

  textbox: {
    width: '80%',
    marginVertical: 10,
    padding: 8,
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 4,
    fontSize: 14,
  },

  button: {
    backgroundColor: 'blue',
    padding: 10,
    borderRadius: 4,
    marginTop: 10,
  },
});

export default SignupScreen;

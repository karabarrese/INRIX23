// SignupScreen.tsx
import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';
import { add_contacts } from './addDataToDatabase'; // Adjust the path accordingly
import { getDocID } from './DocIdGetterSetter'

class ContactsScreen extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      parentName: "",
      parentNumber: "",
    };
  }

  handleSubmit = async () => {
    // console.log('Submitted:', this.state.parentName, this.state.parentNumber, getDocID());

    let docID = getDocID();

    add_contacts(this.state.parentName, this.state.parentNumber, docID);
    console.log("Function returned a");
    // this.props.navigation.navigate("Contacts");
    // this.props.navigation.navigate("Contacts");

    return docId;
  };

  render() {
    return (
      <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
        <Text>Contact Screen</Text>

        <TextInput
          value={this.state.parentName}
          onChangeText={(text) => this.setState({ parentName: text })}
          placeholder="Parent Name"
          style={{ height: 40, borderColor: 'gray', borderWidth: 1, marginBottom: 10, paddingHorizontal: 10, width: 200 }}
        />

        <TextInput
          value={this.state.parentNumber}
          onChangeText={(text) => this.setState({ parentNumber: text })}
          placeholder="Parent Number"
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

export default ContactsScreen;

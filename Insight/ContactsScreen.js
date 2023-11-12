// SignupScreen.tsx
import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { View, Text, TextInput, TouchableOpacity, StyleSheet, Image } from 'react-native';
import { add_contacts } from './addDataToDatabase'; // Adjust the path accordingly
import { getDocID, setDocID } from './DocIdGetterSetter'; 

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
    this.props.navigation.navigate("DrivingFact");

    return docId;
  };
  
  render() {
    return (
      <View style={styles.container}>
        <View style={styles.line1}>
        </View>
        <View style={styles.heading}>
          <Image 
              style={styles.image}
              source={require('./assets/Contacts(2).png')}
          />
          <Text
              style={{fontWeight: 'bold', fontSize: 45, left: '40%', bottom: 50, color: '#243E36'}}>
              Contacts
          </Text>
        </View>
        <View style={styles.line2}>
        </View>
        <TextInput
          value={this.state.parentName}
          onChangeText={(text) => this.setState({ parentName: text })}
          placeholder="Parent Name"
          style={styles.textbox}
        />
  
        <TextInput
          value={this.state.parentNumber}
          onChangeText={(text) => this.setState({ parentNumber: text })}
          placeholder="Parent Number"
          style={styles.textbox}
        />
  
        <TouchableOpacity onPress={this.handleSubmit} style={styles.button}>
          <Text style={{ color: 'white', fontWeight: 'bold', fontSize: 25}}>Submit</Text>
        </TouchableOpacity>
  
        <StatusBar style="auto" />
      </View>
    );
  }
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#243E36',
    alignItems: 'center',
    justifyContent: 'center',
  },

  heading: {
    backgroundColor: '#E0EEC6',
    width: 321, 
    height: 126,
    justifyContent: 'center',
    borderRadius: 20
  },

  line1: {
    backgroundColor: '#7CA982',
    width: 213,
    height: 8, 
    marginBottom: 30
  },

  line2: {
    backgroundColor: '#7CA982',
    width: 213,
    height: 8, 
    marginTop: 30, 
    marginBottom: 20
  },

  textbox: {
    width: '80%',
    marginVertical: 10,
    padding: 8,
    borderWidth: 1,
    backgroundColor: '#962626',
    borderRadius: 4,
    borderColor: 'black',
    fontSize: 25,
    fontWeight: 'bold', 
    color: '#E0EEC6'
  },

  button: {
    backgroundColor: '#962626',
    padding: 5,
    borderRadius: 20,
    marginTop: 30,
    height: 50, 
    width: 231, 
    alignItems: 'center',
    justifyContent: 'center'
  },

  image: {
    width: 96, 
    height: 96, 
    left: '5%',
    top: '25%'
  }
});

export default ContactsScreen;

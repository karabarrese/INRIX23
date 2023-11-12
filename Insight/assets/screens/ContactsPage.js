import React from 'react';
import { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, Image} from 'react-native';

export default function ContactsScreen() {
  const [parentName, setName] = useState('');
  const [parentNumber, setNumber] = useState('');

  const handleSubmit = async () => {
    console.log('Submitted:', parentName, parentNumber);
    await add_contacts(parentName, parentNumber); 
    console.log("Function returned")
  };

  return (
    <View style={styles.container}>
      <View style={styles.line1}>
      </View>
      <View style={styles.heading}>
        <Image 
            style={styles.image}
            source={require('../assets/Contacts(2).png')}
        />
        <Text
            style={{fontWeight: 'bold', fontSize: 45, left: '40%', bottom: 50, color: '#243E36'}}>
            Contacts
        </Text>
      </View>
      <View style={styles.line2}>
      </View>
      <TextInput
        value={parentName}
        onChangeText={(text) => setName(text)}
        placeholder="Parent Name"
        style={styles.textbox}
      />

      <TextInput
        value={parentNumber}
        onChangeText={(text) => setNumber(text)}
        placeholder="Parent Phone"
        style={styles.textbox}
      />

      <TouchableOpacity onPress={handleSubmit} style={styles.button}>
        <Text style={{ color: 'white', fontWeight: 'bold', fontSize: 25}}>Submit</Text>
      </TouchableOpacity>

      <StatusBar style="auto" />
    </View>
  );
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
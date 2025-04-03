import React from 'react';
import { Text, View, StyleSheet, Button } from 'react-native';
import { useEffect, useState } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';

const WeatherScreen = ({}) => {
    const [input, setInput] = useState(''); 
 
    const getData = async () => {
        try {
          const value = await AsyncStorage.getItem('lake');
          if (value !== null) {
            setInput(value); 
          }
        } catch (e) {
          alert("Failed");
        }
    };

    useEffect(() => {
        getData();
    }, [input]); 

    return (
        <View style={styles.container}>
            <Text style={styles.text}> Weather For {input}</Text>
        </View>
    )
}

export default WeatherScreen; 

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#ffffff',
      alignItems: 'center',
      justifyContent: 'center',
    },
    text: {
      color: 'black',
      fontSize: 35,
    },
  });
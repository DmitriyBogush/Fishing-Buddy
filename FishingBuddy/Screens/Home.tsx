import React from 'react';
import { useEffect, useState } from 'react';
import { Text, View, StyleSheet, Button } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import *  as Location from "expo-location";

// Calculate the distance between to points on earth. 
function haversine(long: number, lat: number, long1: number, lat1: number) { 
  const toRadians = (degrees:number) => (degrees * Math.PI) / 180; 
  long = toRadians(long); 
  lat  = toRadians(lat);
  long1 = toRadians(long1); 
  lat1 = toRadians(lat1); 

  const difflon = long1 - long;
  const difflat = lat1  - lat;
  const a = 
    Math.sin(difflat / 2) * Math.sin(difflat / 2) + 
    Math.cos(lat) * Math.cos(lat1) * 
    Math.sin(difflon / 2) * Math.sin(difflon / 2);
  const c = 2 * Math.asin(Math.sqrt(a));
  return 6371 * c;
}

const HomeScreen = ({}) => {
    const [closestLake, setLake] = useState(''); 

    const lakes = require('../datasets/lakes.json');

    let index = 0;

    const getLocation = async () => {
      try {
        let { status } = await Location.requestForegroundPermissionsAsync();
  
        if (status !== "granted") {
          return null;
        }
  
        let location = await Location.getCurrentPositionAsync({});
        return {
          lat: location.coords.latitude,
          lon: location.coords.longitude
        }
      } catch (error) {
        console.error("Error requesting location permission:", error);
        return null; 
      }
    };

    const findClosest = async () => {
      const location = await getLocation(); 
      if(!location) return; 
 
      let inf = Infinity;
      for(let i = 0; i < lakes.length; i++)
      {
        let lon2 = lakes[i][1];
        let lat2 = lakes[i][2]; 
        let distance = haversine(lon2, lat2, location.lon, location.lat); 
        if(distance < inf){
          inf = distance; 
          index = i; 
        };
      }

      setLake(lakes[index][0]);
      await AsyncStorage.setItem('lake', lakes[index][0]);
    };

    useEffect(() => {     
      findClosest();
    }, []); 

    return (
        <View style={styles.container}>
            <Text style={styles.text}> Your at {closestLake} </Text>
        </View>
    )
}

export default HomeScreen; 

const styles = StyleSheet.create({
    container: {
      flex: 1,
      // FIX LATER
      backgroundColor: 'white',
      alignItems: 'center',
      justifyContent: 'center',
    },
    text: {
      color: 'black',
      fontSize: 35,
    },
  });
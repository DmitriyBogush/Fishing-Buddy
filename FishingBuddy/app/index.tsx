import { Text, View, StyleSheet, Button } from 'react-native';
import { useEffect, useState } from 'react';

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
    Math.sin(difflon / 2) * Math.sin(difflon / 2)
  const c = 2 * Math.asin(Math.sqrt(a))
  return 6371 * c;
}

export default function Index() {
  const [distance, setDistance] = useState(0); 
  const [inf, setLowest] = useState(1000);
  const [closestLake, setLake] = useState(''); 
  const lakes = require('./lakes.json');
  const currlon = -122.0776839, currlat = 48.011960; 

  const findClosest = () => {
    for(let i = 0; i < lakes.length; i++)
    {
      let lon2 = lakes[i][1];
      let lat2 = lakes[i][2]; 
      if(haversine(lon2, lat2, currlon, currlat) < inf){
        //console.log("Iteration:", i, "Distance was: ", haversine(lon2, lat2, currlon, currlat), "Lowest was: ", inf);
        setDistance(haversine(lon2, lat2, currlon, currlat));
        setLowest(haversine(lon2, lat2, currlon, currlat));
        setLake(lakes[i][0]);
      };
    }
  };

  useEffect(() => {
    findClosest();
  }, [closestLake]); 


  return (
    <View style={styles.container}>
      <Button title="Click Here" onPress={findClosest}/>
      <Text style={styles.text}>Home screen {inf} {closestLake}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#25292e',
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    color: '#fff',
  },
});


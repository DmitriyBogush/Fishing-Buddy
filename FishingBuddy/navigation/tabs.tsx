import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { Text, View, StyleSheet, Button, Image } from 'react-native';

import HomeScreen from '../Screens/Home'; 
import WeatherScreen from "@/Screens/Weather";

const Tab = createBottomTabNavigator(); 

const Tabs = () => {
    return(
        <Tab.Navigator
        screenOptions={{
            tabBarShowLabel: false,
            tabBarStyle: {
                position: 'absolute',
                bottom: 0, 
                marginLeft: 20, 
                marginRight: 20, 
                borderRadius: 15, 
                elevation: 0, 
                backgroundColor: 'white',
                borderTopWidth: 0, 
                height: 90,
            }
        }}
        >
            <Tab.Screen name="Home" component={HomeScreen} options={{ 
                headerShown: false, 
                tabBarIcon: ({focused}) => (
                    <View style={{alignItems:'center', justifyContent:'center', top:15}}>
                        <Image 
                            source={require('../assets/icons/house-icon.png')}
                            resizeMode="contain"
                            style={{
                                width:30, 
                                height: 30,
                                tintColor: focused ? 'blue' : 'black'
                            }} />
                        
                    </View>
                ),}}/>
            
            <Tab.Screen name="Weather" component={WeatherScreen} options={{ 
                headerShown: false, 
                tabBarIcon: ({focused}) => (
                    <View style={{alignItems:'center', justifyContent:'center', top:15}}>
                        <Image 
                            source={require('../assets/icons/cloud-wind-icon.png')}
                            resizeMode="contain"
                            style={{
                                width:30, 
                                height: 30,
                                tintColor: focused ? 'blue' : 'black'
                            }} />
                        
                    </View>
                ),}}/>
        </Tab.Navigator>
    )
}

export default Tabs; 

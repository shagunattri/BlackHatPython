import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:audioplayers/audio_cache.dart';

void main() => runApp(XylophoneApp());




class XylophoneApp extends StatelessWidget {

  void sound(int no){
    final player = AudioCache();
    player.play('note$no.wav');
  }

  Expanded buildnote({Color color,int no}) {
    return Expanded(
      child: FlatButton(
        color: color,
        onPressed: () {
          sound(no);
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.blueAccent,
        body: SafeArea(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              buildnote(color:Colors.red,no:1),
              buildnote(color:Colors.blue,no:2),
              buildnote(color:Colors.green,no:3),
              buildnote(color:Colors.yellow,no:4),
              buildnote(color:Colors.purple,no:5),
              buildnote(color:Colors.orange,no:6),
              buildnote(color:Colors.indigo,no:7),
            ],
          ),
        ),
      ),
    );
  }
}

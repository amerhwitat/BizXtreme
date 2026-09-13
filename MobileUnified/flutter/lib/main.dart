import 'package:flutter/material.dart';
import 'mobile_game_state.dart';

void main() => runApp(const BizXtremeMobileApp());

class BizXtremeMobileApp extends StatelessWidget {
  const BizXtremeMobileApp({super.key});
  @override
  Widget build(BuildContext context) {
    final state = MobileGameEngine.start(mode: 'tycoon');
    return MaterialApp(home: Scaffold(body: Center(child: Text('BizXtreme • ${state.mode} • BIZ • Cash ${state.cash}'))));
  }
}

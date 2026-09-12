import 'package:flutter/material.dart';

void main() => runApp(const BizXtremeApp());

class BizXtremeApp extends StatelessWidget {
  const BizXtremeApp({super.key});
  @override
  Widget build(BuildContext context) => MaterialApp(
    title: 'BizXtreme',
    home: Scaffold(
      appBar: AppBar(title: const Text('BizXtreme Game Hub')),
      body: ListView(children: [
        _item(context, '2D Storyboard Adventure', '2D'),
        _item(context, '3D World Builder', '3D'),
        _item(context, '4D Timeline Quest', '4D'),
        _item(context, 'Wallet Setup & Backup', 'Wallet'),
        _item(context, 'Snapshots & Saves', 'Saves'),
        _item(context, 'Hall of Fame', 'Scores'),
        _item(context, 'Friends / Peer Presence', 'Network'),
        _item(context, 'Free & Low-Cost Store', 'Store'),
      ]),
    ),
  );
  static Widget _item(BuildContext c, String title, String tag) => ListTile(
    title: Text(title), subtitle: Text(tag), trailing: const Icon(Icons.play_arrow),
    onTap: () => ScaffoldMessenger.of(c).showSnackBar(SnackBar(content: Text('$title selected'))),
  );
}

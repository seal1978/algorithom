final qBuilder = objectbox.eventBox.query(EventBox_.reminderOn.equals(true))..order(EventBox_.start,flags: Order.descending);
final query = qBuilder.build();
    final boxes = (query..limit=60).find();
    return _boxes2events(boxes);

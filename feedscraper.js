var transactionPeople = $.map($('.p_ten_l.p_ten_b .m_five_t.p_ten_r'), function(transaction) {
  return [$.map($(transaction).find('a'), function(person) {
    return person.text;
  })];
});

var i;
for (i = 0; i < transactionPeople.length; i++) {
  var pair = transactionPeople[i];
  console.log(i, pair[0], ':', pair[1]);
}
